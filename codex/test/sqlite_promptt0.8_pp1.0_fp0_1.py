import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:') for a database that exists only in memory
sqlite_db = sqlite3.connect(':memory:')
sqlite_db.close()

# https://docs.python.org/3/library/ctypes.html
# ctype.c_int means a ctype int which is platform dependent, ctype.c_char_p is a string

class Process(object):
    def __init__(self, pid):
        self.pid = pid
        try:
            self.process_handle = ctypes.windll.kernel32.OpenProcess(access, 0, pid)
        except:
            self.process_handle = None

    def read_bytes(self, addr, num_bytes):
        data = ctypes.create_string_buffer(num_bytes)
        bytes_read = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.ReadProcessMemory(self.process_handle, addr, data, num_bytes, ctypes.byref(bytes_read))
        return data.raw

