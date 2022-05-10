import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def get_data(filename):
    """
    Reads the data from the file and returns it as a list of lists.
    """
    with codecs.open(filename, 'r', 'utf-8', 'replace_with_space') as f:
        lines = f.readlines()
    data = []
    for line in lines:
        data.append(line.split())
    return data

def get_vocab(data):
    """
    Returns the vocabulary of the data as a set.
    """
    vocab = set()
    for line in data:
        for word in line:
            vocab.add(word)
    return vocab

def get_counts(data):
    """
    Returns the counts of the data as a dictionary.
    """
    counts = {}
    for line in data:
        for word in line:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    return counts

def
