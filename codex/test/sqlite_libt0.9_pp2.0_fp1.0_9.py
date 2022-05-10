import ctypes
import ctypes.util
import threading
import sqlite3
import atexit

__all__ = ['ipa', 'init_ipa']

Thread_self = ctypes.CFUNCTYPE(ctypes.py_object)(
    ("thread_self", ctypes.pythonapi))
# @@: THIS IS WRONG:
Thread_get_key = ctypes.CFUNCTYPE(ctypes.c_long, ctypes.py_object,
                                  ctypes.c_int)(
    ("thread_get_key", ctypes.pythonapi))


class IPA_thread(threading.Thread):

    __slots__ = ('ipa', 'interval', 'last')

    def __init__(self, ipa, interval):
        super(IPA_thread, self).__init__()
        self.ipa = ipa
        self.interval = interval
        self.last = 0

    def run(self):
        while 1:
            time.sleep(self.interval - self.last)
            t = time.time()
