import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


class MySQLData(object):

    def __init__(self, host, port, user, password, db, charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.charset = charset
        
    def connect(self):
        connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.db,
            charset=self.charset
        )
        return connection
    
    def query(self, sql, return_dict=True):
        with self.connect() as connection:
            cursor = connection.cursor(
                pymysql.cursors.DictCursor if return_dict else None)
            cursor.execute(sql)
            results = cursor.fetchall()
