import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Set up the database
engine = create_engine('mysql+mysqldb://root:root@localhost:3306/tweet_db?charset=utf8mb4')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Set up the Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Set up the Twitter stream
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # Check if the tweet is in English
        if status.lang == 'en':
            # Get the tweet text
            tweet_text = status.text

            # Check if the tweet is a retweet
            if not tweet_text.startswith('RT'):
                # Get
