import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect() call
sqlite3.connect(':memory:')

import _sqlite3

def test(msg, src, res):
    if src != res:
        print '%s: %r != %r' % (msg, src, res),
        print 'FAILED'
    else:
        print '%s: %r == %r' % (msg, src, res),
        print 'ok'


TIMEOUT_ERROR = 'operation timed out'

def timeout(func, *args, **kwargs):
    from threading import Thread
    class MyThread(Thread):
        def run(self):
            self.exit = func(*args, **kwargs)

    thread = MyThread()
    thread.start()
    try:
        thread.join(2)
    except KeyboardInterrupt:
        pass
    else:
        raise ValueError, TIMEOUT_ERROR
    thread.exit = 'operation canceled'
    return thread.exit

#
# Test _sqlite3 module (threading mode)

t0 = _sqlite3.threadsafety
print
