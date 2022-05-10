import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

import pymysql

class SqlDB:
    def __init__(self, user, password, host, port=None, db=None):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db = db

    def connect(self):
        try:
            if self.port:
                conn = pymysql.connect(user=self.user, password=self.password, host=self.host, port=self.port)
            else:
                conn = pymysql.connect(user=self.user, password=self.password, host=self.host)
            return conn
        except:
            print("Could not connect to MySQL server")
            return None

    def create_db(self, c, db_name):
        c.execute("SHOW DATABASES")
        db_exists = db_name in [x[0] for x
