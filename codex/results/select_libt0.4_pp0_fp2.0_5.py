import select_data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# import data
df = pd.read_csv('../data/raw/train.csv')
df.head()

# select data
df = select_data.select_data(df)
df.head()

# check for missing values
df.isna().sum()

# check for duplicates
df.duplicated().sum()

# check for outliers
sns.boxplot(df['price'])
plt.show()

# check the distribution of the target variable
sns.distplot(df['price'])
plt.show()

# check the correlation between the features and the target variable
corr = df.corr()
sns.heatmap(corr, xticklabels=corr.columns, yticklabels=corr.columns, annot=True)
plt.show()

# check the distribution of the features
#
