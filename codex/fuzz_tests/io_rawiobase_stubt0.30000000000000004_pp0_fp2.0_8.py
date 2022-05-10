import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
        return len(b)
    def seek(self, offset, whence=0):
        return self.f.seek(offset, whence)
    def tell(self):
        return self.f.tell()
    def fileno(self):
        return self.f.fileno()
    def flush(self):
        return self.f.flush()
    def close(self):
        return self.f.close()

import sys
sys.stdin = File(sys.stdin)
sys.stdout = File(sys.stdout)
sys.stderr = File(sys.stderr)

import os
os.environ['PYTHONUNBUFFERED'] = '1'

import time

# import cProfile
# import pstats
# import io
# import tracemalloc

# pr
