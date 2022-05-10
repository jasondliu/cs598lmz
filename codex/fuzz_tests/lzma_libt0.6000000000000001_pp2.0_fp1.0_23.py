import lzma
lzma.open

with open('titanic.csv', 'rb') as f:
    with lzma.open(f, 'rt') as f2:
        df = pd.read_csv(f2)

df.head()

df.shape

df.dtypes

df.isnull().sum()

df.Pclass.value_counts()

df.Sex.value_counts()

df.Age.describe()

df.Fare.describe()

df.Embarked.value_counts()

#%%

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10,5))
df.Survived.value_counts().plot(kind='bar', ax=ax)
ax.set_title('Survived vs Not Survived', fontsize=20)
ax.set_xlabel('Survived', fontsize=15)
ax.set_ylabel('Count', fontsize=15)

fig, ax = plt.subplots(figsize
