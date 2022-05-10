import codecs
codecs.open('pre-trained-embeddings/glove.6B.50d.txt', encoding='utf-8')

embeddings_index = {}
with codecs.open('pre-trained-embeddings/glove.6B.50d.txt', encoding='utf-8') as f:
    print("Loading Glove Model")
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs
    f.close()
    
print('Found %s word vectors.' % len(embeddings_index))


print('Preparing embedding matrix.')

# prepare embedding matrix
num_words = min(MAX_NB_WORDS, len(word_index) + 1)

embedding_matrix = np.zeros((num_words, EMBEDDING_DIM))

for word, i in word_index.items():
    if i >= MAX_NB_
