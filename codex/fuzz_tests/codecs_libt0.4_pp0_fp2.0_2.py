import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def get_tweets(api, username):
    """
    Get all tweets from a user's timeline and write them to a file.
    """
    page = 1
    deadend = False
    print("Getting tweets from @%s" % username)
    with open('%s_tweets.txt' % username, 'w') as f:
        while True:
            tweets = api.user_timeline(username, page=page)
            for tweet in tweets:
                if (datetime.datetime.now() - tweet.created_at).days < 365:
                    f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                            '\n')
            print("Wrote %d tweets to %s_tweets.txt" % (len(tweets), username))
            if not tweets:
                deadend = True
                break
            page += 1
            if page % 15 == 0:

