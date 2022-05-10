import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:").execute("create virtual table if not exists foo using fts4(bar)")
# Test sqlite3.connect(":memory:").execute("create virtual table if not exists foo using fts4(bar, tokenize=unicode61)")


class Error(Exception):
    pass


class SQLITE_ERROR(Error):
    pass


class SQLITE_INTERNAL(Error):
    pass


class SQLITE_PERM(Error):
    pass


class SQLITE_ABORT(Error):
    pass


class SQLITE_BUSY(Error):
    pass


class SQLITE_LOCKED(Error):
    pass


class SQLITE_NOMEM(Error):
    pass


class SQLITE_READONLY(Error):
    pass


class SQLITE_INTERRUPT(Error):
    pass


class SQLITE_IOERR(Error):
    pass


class SQLITE_CORRUPT(Error):
    pass


class SQLITE_NOTFOUND(Error):
    pass


