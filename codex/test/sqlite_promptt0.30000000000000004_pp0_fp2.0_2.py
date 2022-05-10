import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

import sys

if sys.platform == 'win32':
    import win32api
    import win32con
    import win32file
    import pywintypes

class Win32Lock(object):
    def __init__(self, lockname):
        self.lockname = lockname
        self.lock = None

    def acquire(self, blocking=True):
        if self.lock is not None:
            raise RuntimeError('already acquired')
        self.lock = win32file.CreateFile(self.lockname,
                                         win32con.GENERIC_READ | win32con.GENERIC_WRITE,
                                         0, None, win32con.OPEN_ALWAYS,
                                         win32con.FILE_ATTRIBUTE_NORMAL, None)
        win32file.LockFileEx(self.lock, win32con.LOCKFILE_EXCLUSIVE_LOCK, 0, -0x10000, pywintypes.OVERLAPPED())

    def release(self):
        if self.lock is None:
            raise Runtime
