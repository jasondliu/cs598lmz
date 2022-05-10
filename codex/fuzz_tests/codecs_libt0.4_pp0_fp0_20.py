import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

class Database():
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='', db='kim_db', charset='utf8mb4')
        self.cur = self.conn.cursor()
        self.cur.execute("SET NAMES utf8mb4;")
        self.cur.execute("SET CHARACTER SET utf8mb4;")
        self.cur.execute("SET character_set_connection=utf8mb4;")

    def __del__(self):
        self.conn.close()

    def get_data(self, sql, args=None):
        self.cur.execute(sql, args)
        return self.cur.fetchall()

    def execute(self, sql, args=None):
        self.cur.execute(sql, args)
        self.conn.commit()
