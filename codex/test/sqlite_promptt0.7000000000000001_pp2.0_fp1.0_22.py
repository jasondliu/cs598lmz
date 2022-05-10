import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect():
#   sqlite3.connect('file:%s?mode=memory&cache=shared' % (dbfile,))
#
# Test sqlite3.Connection.create_collation():
#   sqlite3.Connection.create_collation('ascii_locale_insensitive', ascii_locale_insensitive)
#   sqlite3.Connection.create_collation('ascii_locale_insensitive_like', ascii_locale_insensitive_like)
#
# Test sqlite3.Connection.enable_load_extension():
#   sqlite3.Connection.enable_load_extension(True)
#   sqlite3.Connection.load_extension('./libsqlitefunctions.so')
#
# Test sqlite3.Cursor.execute():
#   sqlite3.Cursor.execute('SELECT ascii_locale_insensitive(?, ?)', ('a', 'A'))

# Test sqlite3.Cursor.executemany():
#   sqlite3.Cursor.executemany('
