import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def get_tweet_text(tweet):
    tweet_text = tweet['text'].encode('utf-8')
    for url in tweet['entities']['urls']:
        tweet_text = tweet_text.replace(url['url'], url['expanded_url'])
    return tweet_text

def get_tweet_id(tweet):
    return tweet['id']

def get_tweet_time(tweet):
    return tweet['created_at']

def get_tweet_user(tweet):
    return tweet['user']['screen_name']

def get_tweet_user_id(tweet):
    return tweet['user']['id']

def get_tweet_user_followers(tweet):
    return tweet['user']['followers_count']

def get_tweet_user_friends(tweet):
    return tweet['user']['friends_
