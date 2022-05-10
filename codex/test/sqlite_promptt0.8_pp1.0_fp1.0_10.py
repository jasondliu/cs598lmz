import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file:memorydb?mode=memory&cache=shared', uri=True)
# https://www.sqlite.org/threadsafe.html
# https://www.sqlite.org/c3ref/enable_shared_cache.html
# https://docs.python.org/2/library/sqlite3.html
# https://docs.python.org/3/library/sqlite3.html#module-sqlite3
# https://stackoverflow.com/questions/17551916/threaded-sqlite3-with-python
# https://www.sqlite.org/sharedcache.html
# https://stackoverflow.com/questions/8244817/how-to-make-sqlite-threadsafe-in-a-web-server
# https://hackage.haskell.org/package/sqlite-simple-0.4.16.0/docs/Database-SQLite-Simple.html#g:11

# https://stackoverflow.com/questions/11698063/unable-to-open-database-file-file-is-
