import codecs
codecs.register(lambda x: codecs.lookup("utf8") if x == "utf8mb4" else None)


class DBUtil:
    """
    A util class for database manipulation and configuration.
    """

    def __init__(self, type, url="localhost:3306", user="root", password="", charset="utf8mb4"):
        """
        Constructor

        :param user:
        :param password:
        :param charset:
        :param type: local or remote
        :param url:
        """
        self.sql_statement = ""
        self.ret = False
        self.value = None
        self.err = None
        self.conn = None
        self.cur = None
        self.host = url
        self.user = user
        self.password = password
        self.charset = charset
        if type == "local":
            self.port = 3306
            self.get_conn(type)

    def get_conn(self, type):
        """
        Get the database connection according to the type.
