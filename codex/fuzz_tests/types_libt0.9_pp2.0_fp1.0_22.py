import types
types.SimpleNamespace

import pandas as pd
data = pd.read_csv("../csv/raw/titanic_train.csv")
data.head()

#%%
data.shape

#%%
data = data.iloc[:, 1:]
data.shape

#%%
data.dropna(how='any', inplace=True)
data.shape

#%%
data.info()

#%%
data.isnull().sum()

#%%
num_passengers = data.shape[0]
num_survived = data[data['Survived']==1].shape[0]
percent_survived = num_survived / num_passengers * 100
print("Number of passengers on the Titanic: {0}".format(num_passengers))
print("Number of passengers who survived: {0}".format(num_survived))
print("Percentage of population who survived: {0}%".format(percent_survived))

#%%
data.describe()
