import codecs
codecs.register_error('replace_with_space', lambda e: (u' ', e.start + 1))

def get_tweets(tweet_file):
    """
    Given a file of tweet data, return a list of tweets, each
    of which is a list of words.
    """
    tweets = []
    for line in tweet_file:
        tweet = []
        try:
            tweet = json.loads(line)['text']
            tweet = tweet.replace('\n', ' ')
        except:
            continue
        tweet = [word for word in tweet.split(' ')]
        tweets.append(tweet)
    return tweets

def get_words(tweets):
    """
    Given a list of tweets, return a list of all words found in
    those tweets.
    """
    words = []
    for tweet in tweets:
        for word in tweet:
            words.append(word)
    return words

def get_unique_words(words):
    """
    Given a list of words, return a list of the unique words found
    in that list.
