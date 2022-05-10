import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

class MySql():
    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db

    def get_con(self):
        con = pymysql.connect(host=self.host,
                              port=self.port,
                              user=self.user,
                              password=self.password,
                              db=self.db,
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
        cur = con.cursor()
        if not cur:
            print('connect mysql error.')
            return False
        else:
            return cur
    def close_con(self, cur):
        cur.close()

    def execute_sql(self, sql):
        ret = 0
        try:

