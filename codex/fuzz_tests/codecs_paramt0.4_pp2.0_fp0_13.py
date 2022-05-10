import codecs
codecs.register_error("strict", codecs.ignore_errors)

# Load the dictionary file
def load_dict(dict_file):
    with codecs.open(dict_file, "r", "utf-8", "ignore") as f:
        return set(line.strip() for line in f)

# Load the stopwords file
def load_stopwords(stopwords_file):
    with codecs.open(stopwords_file, "r", "utf-8", "ignore") as f:
        return set(line.strip() for line in f)

# Load the word2vec model
def load_word2vec(word2vec_file):
    # Load the word2vec model
    model = KeyedVectors.load_word2vec_format(word2vec_file, binary=True)
    return model

# Load the word2vec model
def load_word2vec_text(word2vec_file):
    # Load the word2vec model
    model = KeyedVectors.load_word2vec_format(word2vec_file, binary=False)

