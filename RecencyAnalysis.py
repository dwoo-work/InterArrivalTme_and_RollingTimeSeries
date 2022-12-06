import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

sales = pd.read_csv('https://raw.githubusercontent.com/dwoo-work/RecencyAnalysis/main/src/sales_data_sample_utf8.csv')

sales = sales.drop_duplicates()
sales = sales.dropna(subset=['SALES', 'ORDERDATE'],how='any')
sales.info()

# Change ORDERDATE Dtype from object to datetime.

sales['ORDERDATE'] = pd.to_datetime(sales['ORDERDATE'])

# Create new columns within the dataframe.

sales['week'] = sales['ORDERDATE'].dt.week
sales['dayofweek'] = sales['ORDERDATE'].dt.dayofweek
sales['month'] = sales['ORDERDATE'].dt.month
sales['year'] = sales['ORDERDATE'].dt.year

# Create a new column that shows the month and the year

sales['month_year'] = sales['ORDERDATE'].dt.strftime('%B-%Y')

# Identify the last purchase date for each customer

sales['date'] = sales['ORDERDATE'].dt.strftime('%Y-%m-%d')
sales['date'] = pd.to_datetime(sales['date'])

max_date = sales['date'].max()

customer_last = sales.groupby('CUSTOMERNAME').agg(last_purchase_date= ('date','max')).reset_index()
customer_last['recency'] = max_date - customer_last['last_purchase_date']

# Find the MA-7 and MA-14 for the sales data (only populate Aug-2011 data), and show in line chart.

sales_daily = sales.groupby('date').agg(total_sales=('QUANTITYORDERED','sum'))
sales_daily.plot()

sales_daily['moving_7'] = sales_daily.rolling(window = 7).mean()
sales_daily['moving_14'] = sales_daily.total_sales.rolling(window = 14).mean()

sales_daily['2003':'2005'].plot()

# Resample daily sales data into weekly sales data, and show in line chart.

sales_weekly = sales_daily.total_sales.resample('W').sum()
sales_weekly.plot()
