# Inter Arrival Time and Rolling Time Series

This will demonstrate to you how to perform perform inter arrival time analysis, as well as create charts using rolling time series.

This is important, for different supply chain purposes, such as forecasting, performing stock allocation, and visualising sales trend.

#-------------------------------------------------------------------

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install:

- pandas: to perform data administration by pulling in .csv or .xlsx files.
- matplotlib: to perform data visualisation and graphical plotting.

```bash
pip install pandas
pip install matplotlib
```

## Sample Dataset

You can download the sales_data_sample_utf8.csv file from the source folder, which is located [here](https://github.com/dwoo-work/Linear_Regression_Analysis_using_Python/tree/main/src).

Ensure that the file is in CSV UTF-8 format, to avoid UnicodeDecodeError later on.

## The Flow

Firstly, we have to find out if the data is having a normal distribution. This can be done, by using the [Kolmogorov–Smirnov test](https://towardsdatascience.com/kolmogorov-smirnov-test-84c92fb4158d), which will tell us if the sample comes from a population with a specific distribution (in this case, a normal distribution).

Next, if the data follows a normal distribution, we can perform [Linear Regression](https://www.ibm.com/sg-en/topics/linear-regression) to find out the best fit line for the two variables. The first variable is the quantity ordered (demand), and the other variables is the price for each item (price).

Then, once the best fit line is determined, find out the coefficient value, and the intercept value. These two variables will provide you with insight, on the relationship between the demand, and the price.

## Code Explanation

Lines 1-3:  
To import required libraries like Pandas, Numpy, and Scipy
```python   
import pandas as pd
import numpy as np
import scipy.stats as st
```

Lines 5-6:
To import specific functions from Scipy and SKLearn
```python   
from scipy.stats import kstest
from sklearn.linear_model import LinearRegression
```

Line 8:
Read the CSV file
```python   
sales = pd.read_csv('https://raw.githubusercontent.com/dwoo-work/Linear_Regression_Analysis_using_Python/main/src/sales_data_sample_utf8.csv')
```

Line 10-11:
Create list variables to understand file structure.
Line 10 identifies the different kinds of column titles within the CSV file.
Line 11 identifies the different kinds of vehicles that are sold, and compiled within the CSV file.
```python   
columns_list = list(sales)
productLine_list = list(sales['PRODUCTLINE'].unique()))
```

Line 13-14:
Create table variables for each of the product line. For demonstration, we will only be analysing Motorcycles data.
```python   
specific_columns = pd.DataFrame(sales, columns = ["QUANTITYORDERED","PRICEEACH","PRODUCTLINE"])
motorcycles = specific_columns[specific_columns['PRODUCTLINE'].str.match('Motorcycles')]
```

Line 16:
Make Quantity Ordered as an array, because for SKLearn, in order to train the data to use fit method in linear regression, we have to reshape the 1D arrays.
```python   
qtyOrdered = np.array(motorcycles['QUANTITYORDERED'])
```

Line 18-20:
Identify if the motorcycles data is normally distributed

pvalue=0.0774262. As P>0.05, it is reasonable to accept that the quantity ordered is normally distributed.
```python   
mean = qtyOrdered.mean()
sd = qtyOrdered.std()
kstest(qtyOrdered,'norm',args=(mean, sd))
```

Line 22-26:
Identify the relationship between the quantity ordered, and the unit price for motorcycles data.

model.coef_ = array([[0.02305362]]). For every $1 increase in unit price, there is a 0.0231 decrease in demand.

On the other hand, model.intercept_ = array([33.32225513]). If the motorcycle is sold at S0, there will be a demand of 33.3 units.
```python   
x = motorcycles[['PRICEEACH']]
y = motorcycles[['QUANTITYORDERED']]
model = LinearRegression().fit(x,y)
model.coef_
model.intercept_
```

## Credit

Sales Data Sample (https://www.kaggle.com/datasets/kyanyoga/sample-sales-data)

## License

[MIT](https://choosealicense.com/licenses/mit/)