from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.read())

#Reading the data
import pandas as pd
from pandas import DataFrame
df = pd.read_csv('train.csv', sep=',')

#Data cleaning
df['Age'].fillna(df['Age'].mean(), inplace=True)
df.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
df['Sex'].replace(['male', 'female'], [1, 0], inplace=True)
df['Embarked'].replace(['S', 'C', 'Q'], [1, 2, 3], inplace=True)
df.dropna(inplace=True)

#Data preprocessing
X = df.loc[:, ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
y = df.loc[:, ['Survived']]

#Splitting the data
from sklearn.model_selection import train_test_split
X_train, X_test, y
