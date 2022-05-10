import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_texts(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
    return text

def tokenize(text):
    tokens = [word.strip(symbols) for word in text.split()]
    return tokens

def get_words(tokens):
    words = [word.lower() for word in tokens if word.isalpha()]
    return words

def get_bigrams(words):
    bigrams = []
    for i in range(len(words) - 1):
        bigrams.append(words[i] + '_' + words[i + 1])
    return bigrams

def get_trigrams(words):
    trigrams = []
    for i in range(len(words) - 2):
        trigrams.append(words[i] + '_' + words[i + 1] + '_' + words[i + 2])
    return trigrams

def get_ngrams(words, n):
