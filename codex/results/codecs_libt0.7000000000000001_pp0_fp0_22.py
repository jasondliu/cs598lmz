import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)


class Sql:
    def __init__(self, host, user, passwd, db, charset="utf8mb4"):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        self.conn = pymysql.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db,charset=self.charset)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()
        print("关闭数据库连接")

    def select(self, sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        for r in res:
            print(
