import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(...memory..., check_same_thread = False)

class _CursorClass(sqlite3.Cursor):
    def execute(self, statement, *arguments):
        args = []
        for arg in arguments:
            if isinstance(arg, basestring):
                arg = arg.replace(":%", "%")
            args.append(arg)
        return sqlite3.Cursor.execute(self, statement, *args)

def _dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class sqlitewrapper(object):
    def __init__(self, filename = ":memory:"):
        # load sqlite3 if available
        try:
            import sqlite3
        except ImportError:
            pass
        self.conn = sqlite3.connect(filename, check_same_thread = False)
        self.cursor = self.conn.cursor(_CursorClass)
       
