import codecs
codecs.register_error("strict", codecs.ignore_errors)

class Sqlite3Database(Database):
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        self._db = None
        self._cursor = None

    def _connect(self):
        if self._db is None:
            self._db = sqlite3.connect(**self._kwargs)
            self._cursor = self._db.cursor()

    def _disconnect(self):
        if self._db is not None:
            self._db.close()
            self._db = None
            self._cursor = None

    def _execute(self, sql):
        self._connect()
        try:
            self._cursor.execute(sql)
        except sqlite3.DatabaseError as e:
            self._disconnect()
            raise DatabaseError(e)
        self._disconnect()

    def _query(self, sql):
        self._connect()
        try:
            for row in self._cursor.execute(sql):
                yield row
       
