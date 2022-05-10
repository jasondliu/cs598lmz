from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('./data/train.csv.bz2', 'rb').read())

import pandas as pd
df_train = pd.read_csv('./data/train.csv', nrows=1000)
df_train.head(2)

df_train.info()

df_train['comment_text']

df_train['comment_text'].str.len().describe()

df_train['comment_text'].str.split(expand=True).stack().value_counts()

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(min_df=1)
cv_fit = cv.fit_transform(df_train['comment_text'])

cv_fit.toarray()

cv_fit.shape

(df_train['comment_text'].str.len() > 500).mean()

df_train.loc[df_train['comment_text'].str.len() > 500, 'comment_text']

cols = ['toxic', '
