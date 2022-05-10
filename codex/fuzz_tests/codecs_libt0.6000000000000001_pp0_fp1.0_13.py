import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='twitterdb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def process_status(status):
    # Create a cursor to execute queries
    cur = connection.cursor()
    # Check if the tweet is in English
    if hasattr(status, "retweeted_status"):  # Check if Retweet
        try:
            tweet_id = status.retweeted_status.id # Get ID of original tweet
        except AttributeError:  # Not a Retweet
            tweet_id = status.id
    else:
        tweet_id = status.id
    user_id = status.user.id
    coords = status.coordinates
    text = status.text
    created = status.created_at
