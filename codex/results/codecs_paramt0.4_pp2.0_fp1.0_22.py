import codecs
codecs.register_error("strict", codecs.ignore_errors)

class SqliteDatabase(object):
    """
    A wrapper class for sqlite3
    """

    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row

    def execute(self, query, args=None):
        if args is None:
            args = []
        cursor = self.conn.cursor()
        cursor.execute(query, args)
        return cursor

    def executemany(self, query, args):
        cursor = self.conn.cursor()
        cursor.executemany(query, args)
        return cursor

    def select(self, query, args=None):
        cursor = self.execute(query, args)
        return cursor.fetchall()

    def select_one(self, query, args=None):
        cursor = self.execute(query, args)
        return cursor
