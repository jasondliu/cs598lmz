import codecs
codecs.register_error('ignore', codecs.ignore_errors)

def get_tokens(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
        tokens = nltk.word_tokenize(text)
        return tokens

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def get_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in document_words)
    return features

def get_training_set(file_name):
    tokens = get_tokens(file_name)
    word_features = get_word_features(tokens)
    featuresets = [(get_features(token), 'pos') for token in tokens]
    return featuresets

def get_test_set(file_name):
    tokens = get_t
