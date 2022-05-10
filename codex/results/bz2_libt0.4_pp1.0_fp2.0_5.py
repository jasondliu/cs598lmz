import bz2
bz2.BZ2File('data/train.ft.txt.bz2').read(100)

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(input='filename',
                             stop_words='english',
                             max_df=0.5,
                             min_df=10,
                             max_features=5000)

X = vectorizer.fit_transform(['data/train.ft.txt.bz2'])
X.shape

from sklearn.linear_model import LogisticRegression
y = [1 if line.startswith('__label__1') else 0
     for line in bz2.BZ2File('data/train.ft.txt.bz2').readlines()]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = LogisticRegression(C=0.1)
clf.fit(X_train, y_train)


