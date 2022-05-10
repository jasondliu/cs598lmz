import codecs
codecs.register_error('skip', lambda error: (u'', error.end))


def clean_tweet(tweet):
    tweet = tweet.replace('\n', ' ').replace('\r', '').replace('\t', ' ')
    tweet = tweet.replace('"', '').replace('\\', '').replace('/', '').replace('(', '').replace(')', '')
    tweet = tweet.replace('.', '').replace(',', '').replace('?', '').replace('!', '').replace(';', '')
    tweet = tweet.replace(':', '').replace('[', '').replace(']', '').replace('{', '').replace('}', '')
    tweet = tweet.replace('#', '').replace('@', '')
    tweet = tweet.replace('\'', '').replace('\"', '')
    tweet = tweet.replace('&amp;', '')
    tweet = tweet.replace('&lt;', '').replace('&gt;', '')
    tweet = tweet.replace('-', '')
    tweet = tweet.replace('_',
