import ctypes
import ctypes.util
import threading
import sqlite3

my_threading_local = threading.local()

class deleting_conn(sqlite3.Connection):
    def __del__(self):
        self.close()

DB_URI = "file:test?mode=memory"

def my_cb(p):
    a = sqlite3.connect(DB_URI, uri=True, factory=deleting_conn)

    def test_fn(a, b):
        return a

    a.create_function("test", 2, test_fn)

    my_threading_local.a = a

    return 1

def new_sqlite3_prepare_v2(lib):
    sqlite3_prepare_v2 = lib.sqlite3_prepare_v2

    class PreparedStatementWrapper(object):
        """
        A wrapper object for sqlite prepared statements.
        """
        def __init__(self, db, sql, statement):
            """
            Creates a new PreparedStatementWrapper instance.

            :param sqlite3.Connection db: the parent database.
            :param string sql: the SQL command this statement is wrapping.
            :param statement: the prepared sqlite3 statement.
            """
            self.db = db
            self.sql = sql
            self.statement = statement

        def close(self):
            """
            Closes the prepared statement.
            """
            sqlite3.sqlite_statement.close(self)

        def execute(self, *params):
            """
            Executes this SQL statement with the parameters given.
            """
            param_ids = []
