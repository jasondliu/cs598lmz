import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

# Load the word embeddings
word_embeddings = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

# Load the training set
train_posts = numpy.load('train_posts.npy')
train_tags = numpy.load('train_tags.npy')

# Create a dictionary of words in the vocabulary
vocab_dict = {}
for i, vec in enumerate(word_embeddings.vocab):
    vocab_dict[vec] = i

# Load the test set
test_posts = numpy.load('test_posts.npy')
test_tags = numpy.load('test_tags.npy')

# Create a dictionary of words in the vocabulary
vocab_dict = {}
for i, vec in enumerate(word_embeddings.vocab):
    vocab_dict[vec] = i

# Define the model
model = Sequential()
model.add(Emb
