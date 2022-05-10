import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

def get_tweets(filename):
    tweets = []
    with codecs.open(filename, 'r', 'utf-8', 'replace_with_space') as f:
        for line in f:
            tweets.append(line)
    return tweets

def get_tweets_with_emoticons(filename):
    tweets = []
    emoticons = []
    with codecs.open(filename, 'r', 'utf-8', 'replace_with_space') as f:
        for line in f:
            tweet = []
            emoticon = []
            for word in line.split():
                if word.startswith(':') and word.endswith(':'):
                    emoticon.append(word)
                else:
                    tweet.append(word)
            tweets.append(' '.join(tweet))
            emoticons.append(emoticon)
    return tweets, emoticons

def get_tweets_with_labels(filename):
   
