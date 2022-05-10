import codecs
codecs.register_error('ignore', codecs.ignore_errors)

def get_tweets(tweet_file):
    tweets = []
    for line in tweet_file:
        tweets.append(json.loads(line))
    return tweets

def get_terms(tweets):
    terms = []
    for tweet in tweets:
        if 'text' in tweet:
            terms.extend(tweet['text'].split())
    return terms

def get_sentiment(sent_file):
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores

def get_score(term, scores):
    if term in scores:
        return scores[term]
    else:
        return 0

def get_sentiment_score(terms, scores):
    sentiment_score = 0
    for term in terms:
        sentiment_score += get_score(term, scores)
    return sentiment_score

def get_sentiment_scores(terms, scores):

