import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(file_name):
    data = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip().split('\t')
            data.append(line)
    return data

def get_vocab(data):
    vocab = []
    for line in data:
        for word in line:
            if word not in vocab:
                vocab.append(word)
    return vocab

def get_vocab_dict(vocab):
    vocab_dict = {}
    for i, word in enumerate(vocab):
        vocab_dict[word] = i
    return vocab_dict

def get_vocab_size(vocab):
    return len(vocab)

def get_word_embedding(vocab, embedding_file):
    word_embedding = np.zeros((len(vocab), 300))
    with open(embedding_file, 'r') as f:
        for
