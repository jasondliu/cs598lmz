import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

#import logger

libc = ctypes.CDLL(ctypes.util.find_library('c'))
libc.prctl(1, 16, 0, 0, 0)

log = logging.getLogger(__name__)

class _ThreadWithExc(threading.Thread):
    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.exc = None

    def run(self):
        try:
            if hasattr(self, '_Thread__target'):
                self._Thread__target(*self._Thread__args, **self._Thread__kwargs)
            else:
                self._target(*self._args, **self._kwargs)
        except Exception as e:
            self.exc = e

    def join(self):
        threading.Thread.join(self)
        if self.exc:
            raise self.exc

class ThreadWithExc(_ThreadWithExc):
    def __init__(self, group=
