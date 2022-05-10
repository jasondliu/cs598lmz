import codecs
codecs.register_error('ignore', codecs.lookup('utf-8'))

def load_vocab(vocab_path):
    """Loads a vocabulary file into a dictionary."""
    vocab = collections.OrderedDict()
    index = 0
    with tf.gfile.GFile(vocab_path, "r") as reader:
        while True:
            token = reader.readline()
            if not token:
                break
            token = token.strip()
            vocab[token] = index
            index += 1
    return vocab


def convert_by_vocab(vocab, items):
    """Converts a sequence of [tokens|ids] using the vocab."""
    output = []
    for item in items:
        output.append(vocab[item])
    return output


n_hidden = 128  # hidden layer num of features
n_classes = 2  # linear sequence or not
n_inputs = 50
batch_size = 512

X = tf.placeholder("float", [None, n_inputs, 1])
Y = tf
