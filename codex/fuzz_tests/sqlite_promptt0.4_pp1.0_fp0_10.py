import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
#   1. sqlite3.connect()
#   2. sqlite3.connect(":memory:")
#   3. sqlite3.connect("")
#   4. sqlite3.connect("file:")
#   5. sqlite3.connect("file:test.db")
#   6. sqlite3.connect("file:test.db?mode=memory")
#   7. sqlite3.connect("file:test.db?mode=memory&cache=shared")
#   8. sqlite3.connect("file::memory:")
#   9. sqlite3.connect("file::memory:?cache=shared")
#  10. sqlite3.connect("file:test.db", uri=True)
#  11. sqlite3.connect("file:test.db?mode=memory", uri=True)
#  12. sqlite3.connect("file:test.db?mode=memory&cache=shared", uri=True)
#  13. sqlite3.connect("file::memory:", uri=True)
#  14
