import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

class Mysql():
    def __init__(self):
        self.conn = pymysql.connect(
            host='localhost',
            user='root',
            passwd='123456',
            db='test',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    def save_to_mysql(self, result):
        for i in result:
            url = i[0]
            title = i[1]
            content = i[2]
            sql = "insert into test(url,title,content) values('%s','%s','%s')" % (url, title, content)
            try:
                self.cur.execute(sql)
                self.conn.commit()
            except Exception as e:
                print(e)
                self.conn.rollback()

    def close_
