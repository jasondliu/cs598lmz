import bz2
bz2_file = bz2.BZ2File('data/train.csv.bz2')
data = pd.read_csv(bz2_file)
data.head()

data.describe()

data.shape

data.info()

data.columns

data.isnull().sum()

data.dtypes

data['Survived'].value_counts()

data['Pclass'].value_counts()

data['Sex'].value_counts()

data['Embarked'].value_counts()

data['Age'].value_counts()

data['SibSp'].value_counts()

data['Parch'].value_counts()

data['Fare'].value_counts()

data['Cabin'].value_counts()

data['Ticket'].value_counts()

data['Name'].value_counts()

data[data['Embarked'].isnull()]

data[data['Age'].isnull()]

data
