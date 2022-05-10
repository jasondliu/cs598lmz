import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
    def read(self, size=-1):
        return b"A" * size
    def write(self, b):
        pass
    def seek(self, offset, whence=0):
        pass
    def tell(self):
        return 0
    def close(self):
        pass
    def fileno(self):
        return 0
    def flush(self):
        pass
    def isatty(self):
        return False
    def readable(self):
        return True
    def seekable(self):
        return True
    def writable(self):
        return True

file = File("/dev/null")

import sys
sys.stdin = file
sys.stdout = file
sys.stderr = file

import os
os.environ = {}

import time
time.time = lambda: 0

import _thread
_thread.start_new_thread = lambda *args, **kwargs: 0

import _thread
_thread.start_new_thread =
