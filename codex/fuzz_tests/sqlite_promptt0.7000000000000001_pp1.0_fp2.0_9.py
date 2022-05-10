import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect (':memory:')

def get_libc():
    """
    Attempt to load libc. On some platforms, this may take some time
    and the application may appear to be unresponsive.
    """
    libc_name = None
    if sys.platform == 'darwin':
        libc_name = 'libc.dylib'
    elif sys.platform == 'win32':
        libc_name = 'msvcrt'
    else:
        libc_name = ctypes.util.find_library('c')
        if not libc_name:
            libc_name = 'libc.so.6'

    return ctypes.CDLL(libc_name)

class ThreadInterrupt(Exception):
    pass

class SignalThread(threading.Thread):
    """
    This thread waits for a signal to be delivered and interrupts
    the main thread.
    """
    def __init__(self, signo):
        super(SignalThread, self).__init__()
        self.signo = signo
        self._libc =
