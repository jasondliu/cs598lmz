import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def get_data(data_file):
    with codecs.open(data_file, encoding='utf-8', errors='replace_with_space') as f:
        data = f.readlines()
        data = [d.strip() for d in data]
        data = [d.split('\t') for d in data]
        data = [d for d in data if len(d) == 2]
        return data

def get_vocab(data):
    vocab = {}
    for d in data:
        for w in d[0].split():
            if w not in vocab:
                vocab[w] = 1
            else:
                vocab[w] += 1
    return vocab

def get_idx(vocab, vocab_size):
    idx = {}
    idx['<PAD>'] = 0
    idx['<UNK>'] = 1
    idx['<START>'] = 2
    idx['<END>'] =
