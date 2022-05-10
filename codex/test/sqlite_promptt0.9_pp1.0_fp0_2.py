import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
# Test sqlite3.connect('../src/sqlite3')

libc = ctypes.CDLL(ctypes.util.find_library('c'))

def p(string) :
    print (string)

def thread(arg) :
    if libc.pthread_setcancelstate(0, 0) != 0 :
        p('Cannot call pthread_setcancelstate')

    conn = sqlite3.connect('../src/sqlite3')
    curs = conn.cursor()
    curs.execute(arg)

    p('exiting')
    sys.stdout.flush()

class Cancelled(RuntimeError) : pass
def checkCancelled(result, func, args) :
    if result == -1 :
        err = ctypes.get_errno()
        if err == ctypes.c_int(4).value : # EINTR
            raise Cancelled
        else :
            locate = libc.__errno_location()
