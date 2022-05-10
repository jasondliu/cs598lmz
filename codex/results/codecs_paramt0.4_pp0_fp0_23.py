import codecs
codecs.register_error('replace_with_space', lambda e: (u' ',e.start + 1))

#importing the dataset
data = pd.read_csv('train.csv',encoding='utf-8', error_bad_lines=False, warn_bad_lines=False)

#data = data.drop(['id'], axis=1)

data.head()

#data.shape

#data.isnull().sum()

#data.describe()

#data.info()

#data.columns

#data.dtypes

#data['toxic'].value_counts()

#data['severe_toxic'].value_counts()

#data['obscene'].value_counts()

#data['threat'].value_counts()

#data['insult'].value_counts()

#data['identity_hate'].value_counts()

#data['comment_text'][0]

#data['comment_text'][6]

#data['comment_text'][7]

