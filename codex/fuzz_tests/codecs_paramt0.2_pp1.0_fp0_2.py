import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_data(filename):
    """
    Reads in the data from the given file.
    """
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        data = f.readlines()
    return data

def get_words(data):
    """
    Returns a list of all the words in the data.
    """
    words = []
    for line in data:
        words.extend(line.split())
    return words

def get_word_counts(words):
    """
    Returns a dictionary mapping each word to its count.
    """
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def get_top_words(word_counts, n):
    """
    Returns a list of the top n words and their counts.
    """

