import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect locks

libc_strerror = ctypes.CDLL(ctypes.util.find_library('c')).strerror
libc_strerror.restype = ctypes.c_char_p
libc_strerror.argtypes = [ctypes.c_int]

_mtx = threading.Lock()


class Error(Exception):
    def __init__(self, errno, funcname):
        super(Error, self).__init__(libc_strerror(errno), errno, funcname)


class Connection(sqlite3.Connection):
    def connect(self):
        self.lockec_count = 0
        self.lockec_batch_count = 0
        return self.Connection__connect()

    def _commit(self):
        self.lockec_count += 1
        self.lockec_batch_count += 1
        return self.Connection__commit()

    def _rollback(self):
        self.lockec_count += 1
        self.lockec_batch_count += 1
