import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    data = []
    with codecs.open(filename, encoding='utf-8', errors='strict') as f:
        for line in f:
            data.append(line.strip().split())
    return data

def get_vocab(data):
    vocab = set()
    for line in data:
        for word in line:
            vocab.add(word)
    return vocab

def get_word2idx(vocab):
    word2idx = {}
    for i, word in enumerate(vocab):
        word2idx[word] = i
    return word2idx

def get_idx2word(vocab):
    idx2word = {}
    for i, word in enumerate(vocab):
        idx2word[i] = word
    return idx2word

def get_idx_data(data, word2idx):
    idx_data = []
    for line in data:
        id
