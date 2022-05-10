import ctypes
import ctypes.util
import threading
import sqlite3
import time
import ConfigParser

#
# This started out as a copy and paste of some of the code from sdesk,
# so I'll assume the same license applies.
#
#

class Queue:
    """
    A Queue class, using a ctypes lock.
    """
    def __init__(self):
        self.lock = threading.Lock()
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def enqueue(self, item):
        self.lock.acquire()
        self.queue.append(item)
        self.lock.release()

    def dequeue(self):
        self.lock.acquire()
        item = self.queue.pop(0)
        self.lock.release()
        return item


if sys.platform == 'win32':
    idletime = ctypes.windll.kernel32.GetTickCount
else:
    _idlelib = ctypes.util.find_library("IdleTime")
    if not _idlelib:
