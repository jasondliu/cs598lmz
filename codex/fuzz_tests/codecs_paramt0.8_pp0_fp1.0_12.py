import codecs
codecs.register_error('replace_with_space', codecs.replace_with())

class WordEmbeddings(object):

    def __init__(self, word_embeddings_path, embedding_size, vocab_size=None):
        if embedding_size == 0:
            embedding_size = None
        self.embeddings = self._read_embeddings(word_embeddings_path, embedding_size, vocab_size)
        self.embedding_size = embedding_size

    def _read_embeddings(self, word_embeddings_path, embedding_size, vocab_size):
        print "Reading %s" % word_embeddings_path
        if word_embeddings_path.endswith('.npy'):
            return np.array(np.load(word_embeddings_path))
        else:
            with open(word_embeddings_path, 'r') as f:
                n, dim = f.readline().strip().split()
                print "Creating word embedding matrix %s %s" %
