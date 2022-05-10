import bz2
bz2_file = bz2.BZ2File('data/train.ft.txt.bz2')
raw_data = bz2_file.readlines()
print(raw_data[0])

from sklearn.model_selection import train_test_split
train_raw_data, test_raw_data = train_test_split(raw_data, test_size=0.2, random_state=42)

#%%
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report

text_clf = Pipeline([
    ('vect', CountVectorizer(stop_words='english')),
    ('tfidf', TfidfTransformer()),
    ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=
