import ctypes
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
from IPython.display import Image

#importing dataset
df = pd.read_csv('csv/Salary_Data.csv')
df.head()

#checking dataset info
df.describe()

#data visualization
plt.figure(figsize=(12,6))
sns.scatterplot(x=df.YearsExperience, y=df.Salary)

#data preprocessing
from sklearn.model_selection import train_test_split

#creating an array for independent variable
X = df.iloc[:, :-1].values

#creating an array for dependent variable
y = df.iloc[:, -1].values

#splitting dataset into training set and test set
X_train, X_test, y_train,
