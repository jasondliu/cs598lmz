import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:") - but in a subthread, to avoid the
# "Storage must be an instance of Source or Destination" error seen
# in test_distutils.test_msvccompiler on 64-bit platforms.
def connect_in_subthread():
    try:
        sqlite3.connect(":memory:")
    except sqlite3.OperationalError as e:
        # In older versions of pysqlite, the message is "unable to open
        # database file".  In newer versions, it is "file is encrypted or
        # is not a database".
        return e.args[0].startswith('unable to open database file')
    else:
        return 1
res = threading.Thread(target=connect_in_subthread).start()
_sqlite_finalize_options = None
if sys.platform != "win32":
    RESETARGS = {}
    UNICODEARGS = {'use_unicode': True}
