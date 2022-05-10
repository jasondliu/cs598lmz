import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

class Database:
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = ''
        self.db = 'tweet_db'
        self.charset = 'utf8mb4'
        self.cursorclass = pymysql.cursors.DictCursor

        self.connection = pymysql.connect(host=self.host,
                                          user=self.user,
                                          password=self.password,
                                          db=self.db,
                                          charset=self.charset,
                                          cursorclass=self.cursorclass)
        self.cursor = self.connection.cursor()

    def insert_tweets(self, tweets):
        for tweet in tweets:
            try:
                with self.connection.cursor() as cursor:
                    sql = "INSERT INTO tweets (user_id, user_
