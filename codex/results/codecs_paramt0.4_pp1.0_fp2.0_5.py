import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_tokens(text):
    tokens = []
    for token in text.split():
        if token.startswith('http') or token.startswith('@') or token.startswith('#'):
            continue
        tokens.append(token)
    return tokens

def get_sentiment(tokens):
    sentiment = 0
    for token in tokens:
        if token in positive_words:
            sentiment += 1
        elif token in negative_words:
            sentiment -= 1
    return sentiment

def get_sentiment_score(tweet):
    tokens = get_tokens(tweet)
    return get_sentiment(tokens)

def get_tweets(file_name):
    tweets = []
    with open(file_name, 'r') as f:
        for line in f:
            tweets.append(line)
    return tweets

def get_tweet_sentiment_scores(tweets):
    scores = []
    for tweet in
