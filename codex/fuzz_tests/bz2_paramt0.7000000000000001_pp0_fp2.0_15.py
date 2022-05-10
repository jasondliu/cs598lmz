from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open("../data/train.csv.bz2").read())

train = pd.read_csv("../data/train.csv")
test = pd.read_csv("../data/test.csv")
train.head()

train.info()

train['Age'][0:10]

train['Age'].mean()

train['Age'].median()

train['Fare'].mean()

train['Fare'].median()

train['Pclass'].value_counts()

train['Sex'].value_counts()

train['Survived'].value_counts()

train.describe()

train.describe(include=['O'])

train[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False)

train[["Sex", "Survived"]].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False
