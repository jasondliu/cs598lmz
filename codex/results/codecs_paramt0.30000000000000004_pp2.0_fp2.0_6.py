import codecs
codecs.register_error('ignore', codecs.lookup('utf-8')[3])

def get_data(file_path):
    """
    Reads the data from the file and returns a list of lists.
    """
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            data.append(line.split())
    return data

def get_vocab(data):
    """
    Returns a set of all the words in the data.
    """
    vocab = set()
    for line in data:
        for word in line:
            vocab.add(word)
    return vocab

def get_word_count(data):
    """
    Returns a dictionary of word counts.
    """
    word_count = {}
    for line in data:
        for word in line:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return word_count

def get_word_prob(data):
    """

