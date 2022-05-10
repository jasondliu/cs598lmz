import ctypes
import ctypes.util
import threading
import sqlite3
import time
import datetime

# from http://www.joinc.co.kr/w/man/3/pthread

# Don't try this at home, folks.  Only works with GCC.
class PthreadError(Exception):
    """Errors raised by pthread_* functions."""
    pass

def pthread_errcheck(result, func, args):
    """Raise PthreadError if the result of calling a pthread_* function is
    not 0.
    """
    if result != 0:
        errno = ctypes.get_errno()
        raise PthreadError("%s returned error code %d: '%s'" % (
            func, result, os.strerror(errno)))
    else:
        return args

def pthread_create(func, args, daemon=False):
    """Create and start a thread.

    func: the function to execute in the thread
    args: a tuple of arguments to pass to the function
    daemon: whether the thread should be a daemon thread or not

    Returns the thread object.
    """
   
