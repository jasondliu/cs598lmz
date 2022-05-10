import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 定义基类
class Base:
    def __init__(self, host='localhost', port=3306, db='', usr='root', pwd=''):
        self.host = host
        self.port = port
        self.db = db
        self.usr = usr
        self.pwd = pwd
        self.conn = None
        self.cur = None
        self.connect()

    def connect(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.usr, passwd=self.pwd, db=self.db,
                                        charset='utf8mb4')
            self.cur = self.conn.cursor()
        except pymysql.Error as e:
            print("数据库连接失败！%s" % e
