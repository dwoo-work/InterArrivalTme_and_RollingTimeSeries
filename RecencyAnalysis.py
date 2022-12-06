# To import required libraries like Pandas and Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt

# To import specific functions from Datetime.

from datetime import datetime

# Read the CSV file.

sales = pd.read_csv('sales_data_sample_utf8.csv')

# Remove duplicates and #N/A! from the dataframe.

sales = sales.drop_duplicates()
sales = sales.dropna(subset=['SALES', 'ORDERDATE'],how='any')
sales.info() # For data cleaning, dropping all rows that contain any invalid value is not ideal. The data set has shrunk from 2,823 to 147, which affects the validity of the data. Therefore, an improved methods would be to just drop rows that contain invalid value at specific columns that are related to later's analysis, such as SALES and ORDERDATE

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
