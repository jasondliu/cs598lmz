import codecs
codecs.register_error('ignore', codecs.lookup('utf-8'))

def load_data(file_name):
    """
    Load the data from the file
    :param file_name:
    :return:
    """
    with codecs.open(file_name, 'r', 'utf-8') as f:
        data = f.readlines()
    data = [line.replace('\n', '').split('\t') for line in data]
    return data


def build_vocab(data, vocab_file):
    """
    Build the vocabulary
    :param data:
    :param vocab_file:
    :return:
    """
    vocab = {}
    for line in data:
        for word in line[1].split():
            if word not in vocab:
                vocab[word] = 1
            else:
                vocab[word] += 1
    sorted_vocab = sorted(vocab.items(), key=lambda x: x[1], reverse=True)
    with codecs.open(vocab_file, 'w',
