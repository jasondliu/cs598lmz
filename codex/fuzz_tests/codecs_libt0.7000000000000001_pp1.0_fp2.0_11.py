import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)

# Set the seed for random operations.
# This let our experiments to be reproducible.
RANDOM_SEED = 9999
random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)
tf.compat.v1.set_random_seed(RANDOM_SEED)

# Disable some TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

# Information about the WordNet dataset
#SENTENCE_LEN = 100 # The maximum length of a sentence
BATCH_SIZE = 128 # The number of training examples per batch
#NUM_EPOCHS = 1 # The number of epochs to train
#LEARNING_RATE = 0.1 # The optimization initial learning rate
#NUM_CLASSES = 20 #
