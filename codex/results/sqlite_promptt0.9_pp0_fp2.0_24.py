import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection().__doc__ for new options.
# If the __doc__ has bytes authorizer, then we have the new
# detect_types options.
if isinstance(sqlite3.connect.__doc__, bytes):
    detect_types = sqlite3.PARSE_DECLTYPES
else:
    detect_types = 0

threading._DummyThread._Thread__stop = lambda x: 1

namespace = globals()

# A few more aliases for compatibility with other systems
c = sqlite3
db = sqlite3
sqlite = sqlite3
sqlite3.version = __version__
sqlite3.sqlite_version = sqlite3.sqlite_version.decode(sqlite3.sqlite_encoding)

del __version__


# DB-API requirement: open connection factory
def connect(*args, **kwargs):
    """
    sqlite3.connect(database[, timeout, isolation_level,
                    detect_types, factory, cached_statements, uri])

    Opens a connection to the SQLite database file *database*. You can
