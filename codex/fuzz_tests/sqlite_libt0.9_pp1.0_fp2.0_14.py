import ctypes
import ctypes.util
import threading
import sqlite3 as lite

class Receiver:
    def __init__(self):
        self.has_registered = False
        self._db_handler = LiteHandler()
        self._threads = list()
        self._callbacks = dict()

        self._lock = threading.Lock()

    def _lock_(f):
        def wrapper(self, *args, **kwargs):
            self._lock.acquire()
            try:
                return f(self, *args, **kwargs)
            finally:
                self._lock.release()

        return wrapper

    def register_handler(self, name, callback):
        self._callbacks[name] = callback

    def fire_handler(self, name, *args):
        if not (name in self._callbacks):
            raise KeyError

        self._callbacks[name](*args)

    def destroy(self):
        for thread in self._threads:
            thread.destroy()
            thread.join()

        self._db_handler.destroy()

    @_lock_
    def register_db(self, register):

