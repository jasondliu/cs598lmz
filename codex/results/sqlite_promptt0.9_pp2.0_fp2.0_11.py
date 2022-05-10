import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
if __name__ == "__main__":
    connection = sqlite3.connect(":memory:", timeout=10)
    connection.execute("select * from fake")
elif __name__ == "__loader__":
    # Used when loading the .so files
    connection = None

from .dict import Dict
from .set import Set

# The version of the C code.
VERSION = (1, 4, 7)

# The version string of the C code
VERSION_STRING = "1.4.7"

# The symbol of the function that returns the version string of the C code
_SYMBOL_VERSION_STRING = b'pythreadstate_VERSION'

_SQLITE_THREAD_CLEANUP = """
SELECT
  type,
  name
FROM
  sqlite_master
WHERE
  type in ('table', 'index', 'trigger')
"""

_SQLITE_THREAD_COUNT = """
SELECT
  count(*)
FROM
  sqlite_master
WHERE
  type in ('table', 'index
