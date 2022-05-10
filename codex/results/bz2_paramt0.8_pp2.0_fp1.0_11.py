from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = _safe_decompress

with gzip.open('/content/dataset/glove.840B.300d.txt.gz', 'r') as f:
    glove = np.loadtxt(f, dtype='str', comments=None)

print(glove.shape)

# Create embedding matrix
embedding_matrix = np.zeros((len(word_index)+1, 300))

# Add the words from glove
for word, i in word_index.items():
    try:
        embedding_vector = embeddings_index[word]
        embedding_matrix[i] = embedding_vector
    except KeyError:
        embedding_matrix[i] = np.random.normal(0, np.sqrt(0.25), 300)

# Add the padding word
embedding_matrix[0] = np.zeros(300)

# Check embedding matrix
assert embedding_matrix.shape == (len(word_index)+1, 300)
print(f"Embedding shape: {
