import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    """
    Reads the data from the file and returns a list of lists
    """
    with codecs.open(filename, 'r', encoding='utf-8', errors='strict') as f:
        data = []
        for line in f:
            data.append(line.strip().split('\t'))
    return data

def write_data(filename, data):
    """
    Writes the data to the file
    """
    with codecs.open(filename, 'w', encoding='utf-8', errors='strict') as f:
        for line in data:
            f.write('\t'.join(line) + '\n')

def get_word_counts(data):
    """
    Returns a dictionary of word counts
    """
    word_counts = {}
    for line in data:
        for word in line:
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_
