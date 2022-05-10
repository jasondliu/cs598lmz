import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# load train and test data
train_data = pd.read_csv('train.csv', encoding='utf-8', delimiter='\t', quoting=csv.QUOTE_NONE, error_bad_lines=False)
test_data = pd.read_csv('test.csv', encoding='utf-8', delimiter='\t', quoting=csv.QUOTE_NONE, error_bad_lines=False)

# load the GloVe vectors in a dictionary:
embeddings_index = {}
f = open('glove.6B.100d.txt')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:], dtype='float32')
    embeddings_index[word] = coefs
f.close()

print('Found %s word vectors.' % len(embeddings_index))

# prepare text samples and their labels
print('Processing text dataset')

texts
