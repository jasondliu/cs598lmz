import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:", check_same_thread=False)

# Test sqlite3.connect("file::memory:?cache=shared", check_same_thread=False)

class Thread(threading.Thread):
    def __init__(self, name, func, *args):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)
        self.result = None
        self.exception = None

    def run(self):
        try:
            self.result = self.func(*self.args)
        except Exception as e:
            self.exception = e

        with self.condition:
            self.condition.notify()

    def join(self):
        with self.condition:
            while self.exception is None and self.result is None:
                self.condition.wait()

        if self.exception is not None:
            raise self.exception

       
