import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

def read_corpus(corpus_file, corpus_name):
    """Reads the corpus, and returns a list of words in the corpus.
    The words are converted to all lower case.
    """
    # open the file and read the entire content as a list of words
    corpus = open(corpus_file).read().split()
    # convert all the words to lower case
    corpus = [word.lower() for word in corpus]
    print('Number of words in %s: %d' % (corpus_name, len(corpus)))
    return corpus

def read_stopwords(stopwords_file):
    """Reads the stopwords file and returns a set of stopwords"""
    stopwords = set(open(stopwords_file).read().split())
    print('Number of stopwords: %d' % len(stopwords))
    return stopwords

def create_vocab(corpus, stopwords):
    """Creates a set of all the words in the corpus and
