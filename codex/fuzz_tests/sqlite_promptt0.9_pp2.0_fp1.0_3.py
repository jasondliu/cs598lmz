import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() using threads.
# On Mac OS X, this program crashes with a BUS_ADRALN core dump.
# http://bugs.python.org/issue1336

import atexit
atexit.register(sqlite3.threadsafety)

libc = ctypes.CDLL(ctypes.util.find_library('c'))
uid = ctypes.c_int.in_dll(libc, 'geteuid')
initflag = threading.Event()
# func = ctypes.CFUNCTYPE(None)
def func(*args):
    initflag.set()
    print(args)

def worker(n):
    while not initflag.is_set():
        initflag.wait(0.1)
    conn = sqlite3.connect('/tmp/pytest.db')
    threads.append(threading.get_ident())
    print('worker %s uid = %d' % (n, uid.value))
    conn.execute('delete from fractions' + str(n))
    conn.commit()

threads = []
for i
