import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data():
    data = []
    with open('./data/data.csv', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            data.append(line.strip().split(',')[1:])
    return data


vocab = {}
vocab['<pad>'] = 0
vocab['<unk>'] = 1
vocab['<sos>'] = 2
vocab['<eos>'] = 3

def get_vocab(data):
    for line in data:
        for word in line:
            if word not in vocab:
                vocab[word] = len(vocab)
    return vocab

def get_reverse_vocab(vocab):
    reverse_vocab = {v:k for k, v in vocab.items()}
    return reverse_vocab

def get_index_data(data, vocab):
    index_data = []
    for line in data:
        index_data.append
