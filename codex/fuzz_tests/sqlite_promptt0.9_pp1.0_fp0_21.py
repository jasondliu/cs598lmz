import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect in multiprocessing and determine how it is affected by the
#   existance of a Sqlite3Db class.
#
# Connect to a sqlite3 database and close the socket.  Repeat N times as queried by
#   the terminal.  Note the output message and exit value of the program.
#
#   Note that the program is written to emulate Android, meaning it will disconnect
#   and reconnect if the network is present and between 3G, WCDMA, wifi, and EDGE.
#
#   If the error is only the 'close failed' comments at the top of this file.
#
#   If the error is no connection or other, please mail there errors to
#   'chris.d.stalzer@cchmc.org'

def simple_sqlite3(num, pipe):
    log = 'Log/access.log'
    f = open(log, 'a+')
    f.write('Pipe -> %d\n' % num)
    f.close()

    db = ctypes.util.find_library('sqlite3')
    if db:

