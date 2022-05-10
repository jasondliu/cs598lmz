import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_tokens(text):
    return nltk.word_tokenize(text)

def get_sentences(text):
    return nltk.sent_tokenize(text)

def get_words(text):
    return nltk.word_tokenize(text)

def get_bigrams(text):
    return nltk.bigrams(text)

def get_trigrams(text):
    return nltk.trigrams(text)

def get_ngrams(text, n):
    return nltk.ngrams(text, n)

def get_pos(text):
    return nltk.pos_tag(text)

def get_sentiment(text):
    return nltk.sentiment.util.demo_liu_hu_lexicon(text)

def get_nouns(text):
    return [word for (word, pos) in nltk.pos_tag(text) if pos.startswith('N')]

