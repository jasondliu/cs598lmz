import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    """
    Reads data from a file and returns a list of lists.
    """
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        data = f.readlines()
    data = [line.split() for line in data]
    return data

def get_vocab(data):
    """
    Returns a set of all words in the data.
    """
    vocab = set()
    for line in data:
        for word in line:
            vocab.add(word)
    return vocab

def get_word_counts(data):
    """
    Returns a dictionary of word counts.
    """
    word_counts = {}
    for line in data:
        for word in line:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    return word_counts

def get_word_pro
