import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
versionTuple = sqlite3.version_info

print(versionTuple)

print('sqlite3 version is : {}'.format(sqlite3.version))
print('sqlite3 sqlite_version is : {}'.format(sqlite3.sqlite_version))

# Test for loading of sqlite3 library
# sqlite3.lib uses ctypes
if sqlite3.sqlite_version_info < (3, 5, 0):
    raise RuntimeError('Sqlite3 version is to old, please get it from http://www.sqlite.org/download.html')

print(sqlite3.sqlite_version_info)

# test to see if threading is enabled
print(ctypes.util.find_library('sqlite3'))

print('sqlite3_enable_shared_cache : {}'.format(sqlite3.sqlite_enable_shared_cache))

print('sqlite3.threadsafety : {}'.format(sqlite3.threadsafety))

print('threading.activeCount : {}'.format(threading.activeCount()))
