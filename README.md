# Recency Analysis

For this project, it will demonstrate to you on how to perform recency analysis, using the inter-arrival time. On top of that, we will plot charts using the moving average (MA).

This is important for different supply chain purposes, such as forecasting, performing stock allocation, and visualising sales trend.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install:

- pandas: to perform data administration by pulling in .csv or .xlsx files.
- matplotlib: to perform data visualisation and graphical plotting.
- datetime: to manipulate date and time object data.

```bash
pip install pandas
pip install matplotlib
pip install datetime
```

## Sample Dataset

You can download the sales_data_sample_utf8.csv file from the source folder, which is located [here](https://github.com/dwoo-work/InterArrivalTme_and_RollingTimeSeries/blob/main/src/sales_data_sample_utf8.csv).

Ensure that the file is in CSV UTF-8 format, to avoid UnicodeDecodeError later on.

## The Flow

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius felis tellus.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius felis tellus.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius felis tellus.


## Code Explanation

Lines 1-2:  
To import required libraries like Pandas and Matplotlib.
```python   
import pandas as pd
import matplotlib.pyplot as plt
```

Lines 4:  
To import specific functions from Datetime.
```python   
from datetime import datetime
```

Lines 6:  
Read the CSV file.
```python   
sales = pd.read_csv('https://raw.githubusercontent.com/dwoo-work/RecencyAnalysis/main/src/sales_data_sample_utf8.csv')
```

Lines 8-10:  
Remove duplicates and #N/A! from the dataframe.

For data cleaning, dropping all rows that contain any invalid value is not ideal. The data set has shrunk from 2,823 to 147, which affects the validity of the data.

Therefore, an improved methods would be to just drop rows that contain invalid value at specific columns that are related to later's analysis, such as SALES and ORDERDATE
```python   
sales = sales.drop_duplicates()
sales = sales.dropna(subset=['SALES', 'ORDERDATE'],how='any')
sales.info()
```

Lines 12:  
Change ORDERDATE Dtype from object to datetime.
```python   
sales['ORDERDATE'] = pd.to_datetime(sales['ORDERDATE'])
```

Lines 14-17:  
Create new columns within the dataframe.
```python   
sales['week'] = sales['ORDERDATE'].dt.week
sales['dayofweek'] = sales['ORDERDATE'].dt.dayofweek
sales['month'] = sales['ORDERDATE'].dt.month
sales['year'] = sales['ORDERDATE'].dt.year
```

Lines 19:  
Create a new column that shows the month and the year.
```python   
sales['month_year'] = sales['ORDERDATE'].dt.strftime('%B-%Y')
```

Lines 21-25:  
Identify the last purchase date for each customer.
```python   
sales['date'] = sales['ORDERDATE'].dt.strftime('%Y-%m-%d')
sales['date'] = pd.to_datetime(sales['date'])
max_date = sales['date'].max()
customer_last = sales.groupby('CUSTOMERNAME').agg(last_purchase_date= ('date','max')).reset_index()
customer_last['recency'] = max_date - customer_last['last_purchase_date']
```

Lines 27-30:  
Find the MA-7 and MA-14 for the sales data (only populate 2003 - 2005 data), and show in line chart.
```python   
sales_daily = sales.groupby('date').agg(total_sales=('QUANTITYORDERED','sum'))
sales_daily['moving_7'] = sales_daily.rolling(window = 7).mean()
sales_daily['moving_14'] = sales_daily.total_sales.rolling(window = 14).mean()
sales_daily['2003':'2005'].plot()
```

Lines 32-33:  
Resample daily sales data into weekly sales data, and show in line chart.
```python   
sales_weekly = sales_daily.total_sales.resample('W').sum()
sales_weekly.plot()
```

## Credit

Sales Data Sample (https://www.kaggle.com/datasets/kyanyoga/sample-sales-data)

## License

[MIT](https://choosealicense.com/licenses/mit/)