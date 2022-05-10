import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# %%
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=1)

# %%
content = ["How to format my hard disk", " Hard disk format problems "]
X = vectorizer.fit_transform(content)
vectorizer.get_feature_names()

# %%
X.toarray().transpose()

# %%
bigram_vectorizer = CountVectorizer(ngram_range=(1, 2), token_pattern=r'\b\w+\b', min_df=1)
analyze = bigram_vectorizer.build_analyzer()
analyze('Bi-grams are cool!') == (['bi', 'grams', 'are', 'cool', 'bi grams', 'grams are', 'are cool'])
X_2 = bigram_vectorizer.fit_transform(content).toarray()
X_2

# %%
feature_index = bigram_vectorizer.
