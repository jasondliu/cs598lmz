import _struct
os.environ["CUDA_VISIBLE_DEVICES"] = "3"
TRAIN_FILE = './data/train.txt'

VOCAB_FILE = './data/vocab.json'

NUM_CLASSES = 2

NUM_EPOCHS = 10

BATCH_SIZE = 128

NUM_STEPS = 1000

EMBED_SIZE = 300

HIDDEN_SIZE = 300

KEEP_PROB = 0.5

LEARNING_RATE = 0.001

LEN_EXAMPLES = 20000

eval_interval_steps = 100
print_interval_steps = 100
class DataReader(object):
    
    def __init__(self, data_file, num_epochs=10, batch_size=128, num_steps=1000, vocab_file=VOCAB_FILE):
        self._raw_data = codecs.open(data_file, 'r', 'utf-8').read()
        self._data = []
