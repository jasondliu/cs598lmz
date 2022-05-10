import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:') for in-memory database

from .core import *
from .sync import *
from .utils import *


def pthread_join_with_timeout(tid, timeout):
    # call pthread_join with a timeout
    res = pthread_join(tid, timeout)
    if res != 0:
        raise TimeoutError("pthread_join return %d"%res)
    return r

class Process(object):
    """Base class to encapsulate a process.

    Each process is associated with a thread, whose id is in `tid`.
    """
    def __init__(self, tid):
        self.tid = tid

    def join(self, timeout_sec=None):
        """Join the associated thread and check it exits normally.

        After thread exits, this function will wait at most
        `timeout_sec` seconds for the thread to exit. By default,
        wait indefinitely.
        """
        if timeout_sec is None:
            pthread_join(self.tid, None)
        else:
            pthread_join_
