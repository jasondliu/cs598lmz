import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

__all__ = ["connect", "OPENDB", "OPENCREATE", "OPENEXCLUSIVE",
           "OPENREAD", "OPENREADWRITE", "OPENURI", "SQLITE_MAX_ATTACHED",
           "SQLITE_MAX_COLUMN", "SQLITE_MAX_DRIVER_CONNECTIONS",
           "SQLITE_MAX_EXPR_DEPTH", "SQLITE_MAX_LENGTH", "SQLITE_MAX_SQL_LENGTH",
           "SQLITE_MISUSE", "SQLITE_OK", "SQLITE_ROW", "SQLITE_STMTSTATUS_FULLSCAN_STEP",
           "SQLITE_STMTSTATUS_SORT", "SQLITE_DENY", "SQLITE_IGNORE",
           "SQLITE_PRAGMA_FOREIGN_KEYS",
           "PARSE_DECLTYPES", "PARSE_COLNAMES", "threadsafety",
           "DatabaseError", "Warning", "Error", "InterfaceError",
           "DatabaseError", "DataError", "Oper
