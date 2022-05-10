import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

class Database:
    def __init__(self, host, user, password, db, port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port
        self.connection = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, port=self.port)

    def query(self, query):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
        except Exception as e:
            print(e)
            self.connection.rollback()

    def query_fetchone(self, query):
        try:
            with self.connection.cursor() as cursor:
                cursor.
