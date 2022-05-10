import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

class DBConnClass():
    # 初始化数据库连接，默认使用root用户登录
    def __init__(self, dbType, host='127.0.0.1', port=3306, user='root', passwd='root', db='', charset='utf8'):
        self.dbType = dbType
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset

    # 执行数据库操作（增、删、改）
    def do_execute(self, sql):
        db = pymysql.connect(self.host, self.user, self.passwd, self.db
