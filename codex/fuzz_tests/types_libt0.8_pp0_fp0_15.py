import types
types.IntType = int
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
from functools import reduce
from sklearn.preprocessing import OneHotEncoder
import numpy as np
# Setting working directory
os.chdir("/home/mohit/my_projects/my_project_env/practice/6_association_rules")

df = pd.read_excel("Online Retail.xlsx")
df.head()

#Number of unique Country
len(np.unique(df.Country))

#Number of unique stock code
len(np.unique(df.StockCode))

#Number of items purchased for each country
count_country = df.Country.value_counts().reset_index()
count_country.columns = ["Country", "Count"]
count_country

#Number of items purchased for each stock
count_StockCode = df.StockCode.value_counts().reset_index()
count_StockCode.columns = ["StockCode", "Count"]
count_StockCode

## Feature engineering

