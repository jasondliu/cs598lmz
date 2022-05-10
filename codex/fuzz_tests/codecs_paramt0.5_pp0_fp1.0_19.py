import codecs
codecs.register_error('ignore', codecs.replace_errors)

def get_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

def get_api():
    config = get_config()
    key = config['key']
    secret = config['secret']
    api = twitter.Api(
        consumer_key=key,
        consumer_secret=secret,
        access_token_key=key,
        access_token_secret=secret
    )
    return api

def get_tweets(api, query, count=10):
    tweets = api.GetSearch(term=query, count=count)
    return tweets

def get_tweet_ids(tweets):
    ids = []
    for t in tweets:
        ids.append(t.id)
    return ids

def get_tweet_texts(tweets):
    texts = []
    for t in tweets:
        texts.append(t.text)
    return texts

def get_t
