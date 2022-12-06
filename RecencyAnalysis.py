import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

sales = pd.read_csv('https://raw.githubusercontent.com/dwoo-work/RecencyAnalysis/main/src/sales_data_sample_utf8.csv')

sales = sales.drop_duplicates()
sales = sales.dropna(subset=['SALES', 'ORDERDATE'],how='any')
sales.info()

sales['ORDERDATE'] = pd.to_datetime(sales['ORDERDATE'])

sales['week'] = sales['ORDERDATE'].dt.week
sales['dayofweek'] = sales['ORDERDATE'].dt.dayofweek
sales['month'] = sales['ORDERDATE'].dt.month
sales['year'] = sales['ORDERDATE'].dt.year

sales['month_year'] = sales['ORDERDATE'].dt.strftime('%B-%Y')

sales['date'] = sales['ORDERDATE'].dt.strftime('%Y-%m-%d')
sales['date'] = pd.to_datetime(sales['date'])
max_date = sales['date'].max()
customer_last = sales.groupby('CUSTOMERNAME').agg(last_purchase_date= ('date','max')).reset_index()
customer_last['recency'] = max_date - customer_last['last_purchase_date']

sales_daily = sales.groupby('date').agg(total_sales=('QUANTITYORDERED','sum'))
sales_daily['moving_7'] = sales_daily.rolling(window = 7).mean()
sales_daily['moving_14'] = sales_daily.total_sales.rolling(window = 14).mean()
sales_daily['2003':'2005'].plot()

sales_weekly = sales_daily.total_sales.resample('W').sum()
sales_weekly.plot()