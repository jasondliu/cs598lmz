import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)


class Sql(object):
    _connect = None
    _cursor = None
    _connect_args = {}

    def __init__(self, *args, **kwargs):
        self._connect_args = kwargs

    @property
    def connect(self):
        if not self._connect:
            self._connect = pymysql.Connect(**self._connect_args)
            self._cursor = self._connect.cursor(cursor=pymysql.cursors.DictCursor)
        return self._connect

    @property
    def cursor(self):
        if not self._cursor:
            self._connect = pymysql.Connect(**self._connect_args)
            self._cursor = self._connect.cursor(cursor=pymysql.cursors.DictCursor)
        return self._cursor

    def execute(self, sql, **kwargs):
        """
       
