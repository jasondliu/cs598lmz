import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

class DB_manager(object):
    def __init__(self):
        self.connection = pymysql.connect(host=Config.DB_HOST, port=Config.DB_PORT,
                                          user=Config.DB_USER, password=Config.DB_PASSWORD,
                                          db=Config.DB_NAME, charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)

    def get_connection(self):
        return self.connection

    def close_connection(self):
        self.connection.close()
