import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Set up database
engine = create_engine('mysql+mysqldb://root:@localhost:3306/tweets?charset=utf8mb4')
Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Set up Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Set up Twitter stream
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # Get tweet text
        tweet_text = status.text
        # Get tweet id
        tweet_id = status.id
        # Get user id
        user_id = status.user.id
        # Get user screen name
        user_screen_name = status.user.screen
