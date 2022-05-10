import _structs
import _util

#-------------------------------------------------------------------------------

class _Cursor(object):

    def __init__(self, conn, query):
        self._conn = conn
        self._query = query
        self._result = None

    def __del__(self):
        self.close()

    def close(self):
        if self._result is not None:
            self._result.close()
            self._result = None

    def execute(self, query):
        self.close()
        self._result = self._conn._execute(query)

    def fetchone(self):
        if self._result is None:
            self.execute(self._query)
        return self._result.fetchone()

    def fetchall(self):
        if self._result is None:
            self.execute(self._query)
        return self._result.fetchall()

    def fetchmany(self, size=None):
        if self._result is None:
            self.execute(self._query)
        return self._result.fetchmany(size)

#-------------------------------------------------------------------------------
