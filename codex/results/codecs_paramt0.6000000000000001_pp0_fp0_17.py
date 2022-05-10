import codecs
codecs.register_error('ignore', codecs.lookup('ascii'))

class Corpus(object):

    def __init__(self, filename, vocab_size=None, max_vocab_size=None):
        self.vocab_size = vocab_size
        self.max_vocab_size = max_vocab_size
        self.vocab = self.build_vocab(filename, vocab_size, max_vocab_size)
        self.filename = filename

    def build_vocab(self, filename, vocab_size, max_vocab_size):
        vocab = {}
        with codecs.open(filename, 'r', 'utf-8', 'ignore') as f:
            for line in f:
                words = line.strip().split()
                for word in words:
                    if word not in vocab:
                        vocab[word] = 0
                    vocab[word] += 1
        vocab = sorted(vocab.items(), key=lambda x: x[1], reverse=True)
        if vocab_size is not None:
           
