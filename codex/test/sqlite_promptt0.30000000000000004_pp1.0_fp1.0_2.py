import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
conn.commit()
c.close()
# Test ctypes.util.find_library
libc = ctypes.CDLL(ctypes.util.find_library('c'))
libc.time(None)
# Test threading.local
local = threading.local()
local.t = threading.current_thread()
assert local.t is threading.current_thread()
# Test _ctypes
cdll.LoadLibrary(ctypes.util.find_library('c'))
# Test _hashlib
hashlib.md5(b"Nobody inspects the spammish repetition").hexdigest()
# Test _socket
