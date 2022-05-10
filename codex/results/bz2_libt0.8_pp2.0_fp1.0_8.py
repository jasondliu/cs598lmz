import bz2
bz2_file = bz2.BZ2File(corpus_file)

data = []
for line in bz2_file:
    tokens = gensim.utils.tokenize(line, lowercase=True, deacc=True, errors="ignore")
    data.append(tokens)

print('Example of document:')
print(data[1])

print('Number of documents:')
print(len(data))

model_dm = gensim.models.doc2vec.Doc2Vec(data, size = 300, window = 10, min_count = 10, workers=11,iter=55, dm = 1)
model_dbow = gensim.models.doc2vec.Doc2Vec(data, size = 300, window = 10, min_count = 10, workers=11,iter=55, dm = 0)
model_dm.save('model_dm.doc2vec')
model_dbow.save('model_dbow.doc2vec')

new_model_dm = gensim.models.doc2vec.Doc
