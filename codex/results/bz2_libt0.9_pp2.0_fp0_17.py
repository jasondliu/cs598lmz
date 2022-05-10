import bz2
bz2_file = bz2.BZ2File('nlp_data.pickle.bz2')
nlp = pickle.load(bz2_file)
bz2_file.close()
type(nlp)

vocab_size = len(nlp.vocab)
vocab_size
type(nlp.vocab)

# spacy.vocab.Vocab are not subscriptable and therefore not indexable by a vectorizer or a deep learning training function
# convert spacy.vocab.Vocab representations to standard python type str
X_data = [[str(x) for x in doc] for doc in nlp_docs]
example = X_data[0]
print(example)
type(example)
print(example[0])
bigram_vectorizer = CountVectorizer(ngram_range=(1,2))
bigram_vectorizer
bigram_vectorizer.fit(X_data)
X_data_vectorized = bigram_vectorizer.transform(X_data)
type(X_data_vectorized)
print(X_
