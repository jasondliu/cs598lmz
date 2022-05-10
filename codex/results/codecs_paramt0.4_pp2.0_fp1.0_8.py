import codecs
codecs.register_error('strict', codecs.ignore_errors)

# Set up logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Load the model
model = gensim.models.Word2Vec.load(sys.argv[1])

# Load the vocabulary
vocab = model.vocab

# Read the test data
with codecs.open(sys.argv[2], 'r', 'utf-8', 'strict') as f:
    test_data = [line.split() for line in f]

# Evaluate the model
model.accuracy(test_data)

# Compute the similarity between two words
print model.similarity('woman', 'man')

# Compute the similarity between several words
print model.n_similarity(['sushi', 'shop'], ['japanese', 'restaurant'])

# Find the top-N most similar words
print model.most_similar(positive=['woman', 'king'], negative=
