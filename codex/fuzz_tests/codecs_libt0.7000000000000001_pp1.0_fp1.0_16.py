import codecs
codecs.register_error('emoji', codecs.ignore_errors)

import gensim

def __load_stopwords_set(stopwords_file):
    stopwords_set = set()
    for line in open(stopwords_file):
        stopwords_set.add(line.strip())
    return stopwords_set

def is_stopword(word, stopwords_set):
    return True if word in stopwords_set else False

punctuations = string.punctuation
punctuations = punctuations.replace('_', '')
punctuations = punctuations.replace('#', '')
punctuations = punctuations.replace('@', '')

def normalize_tweet(tweet, stopwords_set):
    # Normalize tweet
    tweet = tweet.lower()
    tweet = re.sub(r'http\S+', '<url>', tweet)
    tweet = re.sub(r'#\S+', '<hashtag>', tweet)
    tweet = re.sub(r'@\S+', '<user>',
