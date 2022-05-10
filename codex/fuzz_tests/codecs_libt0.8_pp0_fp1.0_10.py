import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

class MySqlCon(object):
    """mysql数据库操作类"""

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        self.__conn = pymysql.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '123456',
                db = 'reptile_web',
                charset = 'utf8mb4',
                cursorclass = pymysql.cursors.DictCursor
        )

    def __del__(self):
        self.__conn.close()

    def __getcursor(self):
        if self.__conn:
            return self.__conn.
