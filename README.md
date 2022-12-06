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



## Credit

Sales Data Sample (https://www.kaggle.com/datasets/kyanyoga/sample-sales-data)

## License

[MIT](https://choosealicense.com/licenses/mit/)