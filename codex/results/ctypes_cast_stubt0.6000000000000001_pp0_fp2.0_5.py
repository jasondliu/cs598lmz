import ctypes
ctypes.cast(4, ctypes.py_object)

#clear all variables
def clearall():
    all = [var for var in globals() if var[0] != "_"]
    for var in all:
        del globals()[var]

#reset -f
clearall()

#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import dataset
df = pd.read_csv('/Users/krishna/Desktop/DataScience/Datasets/Salary_Data.csv')

#print first 5 rows
df.head()

#print last 5 rows
df.tail()

#print number of rows and columns
df.shape

#print column names
df.columns

#print data types
df.dtypes

#print total missing values
df.isnull().sum()

#print summary statistics
df.describe()

#print unique values in each column
for col in df.columns:
    print(col, df[col].
