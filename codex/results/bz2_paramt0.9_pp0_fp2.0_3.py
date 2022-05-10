from bz2 import BZ2Decompressor
BZ2Decompressor
import pickle
import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# # Merge the two together.
# train = train.set_index('PassengerId')

print(train.head())
# print(train.describe())
# print(train.info())

# train.describe(include=['O'])
#
# train[['Pclass','Survived']].groupby(['Pclass']).mean()
# train[['Sex','Survived']].groupby(['Sex']).mean()
# train[['SibSp','Survived']].groupby(['SibSp']).mean()
# train[['Parch','Survived']].groupby(['Parch']).mean()
#
# g = sns.FacetGrid(train, col='Survived')
# g.map(plt.hist, 'Age', bins=20)
#
# grid = sns.FacetGrid(train,
