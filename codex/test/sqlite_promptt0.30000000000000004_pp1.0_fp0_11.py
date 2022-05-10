import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
# sqlite3.connect('test.db')
# sqlite3.connect(':memory:')
# sqlite3.connect('file:memorydb1?mode=memory&cache=shared', uri=True)
# sqlite3.connect('file:C:\\Users\\Administrator\\Desktop\\test.db?mode=ro', uri=True)
# sqlite3.connect('file:C:\\Users\\Administrator\\Desktop\\test.db?mode=rw', uri=True)
# sqlite3.connect('file:C:\\Users\\Administrator\\Desktop\\test.db?mode=rwc', uri=True)
# sqlite3.connect('file:C:\\Users\\Administrator\\Desktop\\test.db?mode=memory', uri=True)
# sqlite3.connect('file:C:\\Users\\Administrator\\Desktop\\test.db?mode=memory&cache=shared', uri=True)
# sqlite3.connect('file:C:\\Users\\Administrator\\Desktop\\test.db?mode=memory&cache=private', ur
