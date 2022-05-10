import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='twitter',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def process_or_store(tweet):
    print(json.dumps(tweet))

def on_data(data):
    tweet = json.loads(data)
    if 'text' in tweet:
        print(tweet['text'])
    return True

def on_error(status):
    print(status)

if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
   
