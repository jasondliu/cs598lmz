import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

DATA_FILE_PATH = "./data_processed.pkl"

# access twitter API 
auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN_KEY'], os.environ['ACCESS_TOKEN_SECRET'])
api = tweepy.API(auth)

# mysql connection
mysql = MySQLdb.connect(host=os.environ['HOST'], user=os.environ['USER'], passwd=os.environ['PASSWORD'], db=os.environ['DATABASE'], charset='utf8mb4')
cursor = mysql.cursor()

# load data
with open(DATA_FILE_PATH, 'r') as f:
    data = pickle.load(f)

# check if there
