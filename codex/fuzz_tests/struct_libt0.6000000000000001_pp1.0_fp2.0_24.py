import _struct
import _json

from . import _globals

class SQLite3(object):
    def __init__(self, db):
        self._db = db
        self._cursor = None

    def _ensure_cursor(self):
        if self._cursor is None:
            self._cursor = self._db.cursor()

    def _execute(self, *args):
        self._ensure_cursor()
        return self._cursor.execute(*args)

    def _executemany(self, *args):
        self._ensure_cursor()
        return self._cursor.executemany(*args)

    def _fetchone(self):
        return self._cursor.fetchone()

    def _fetchall(self):
        return self._cursor.fetchall()

    def _commit(self):
        self._db.commit()

    def _last_rowid(self):
        return self._cursor.lastrowid

    def _close(self):
        self._cursor.close()
