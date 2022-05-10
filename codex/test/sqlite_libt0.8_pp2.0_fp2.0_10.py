import ctypes
import ctypes.util
import threading
import sqlite3


class Sync:
    def __init__(self):
        self.libc = ctypes.CDLL(ctypes.util.find_library('c'), use_errno=True)
        self.mutex = self.libc.pthread_mutex_init(
            ctypes.byref(ctypes.c_voidp()),
            ctypes.byref(ctypes.c_voidp())
        )
        self.mutex_acquire = self.libc.pthread_mutex_lock
        self.mutex_release = self.libc.pthread_mutex_unlock
        self.cnt = 0

    def acquire(self):
        self.mutex_acquire(self.mutex)

    def release(self):
        self.mutex_release(self.mutex)


class Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.sync = Sync()

    def run(self):
        self.sync.acquire()


