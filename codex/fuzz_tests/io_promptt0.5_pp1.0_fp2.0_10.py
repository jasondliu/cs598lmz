import io
# Test io.RawIOBase
import io
import sys
class TestRawIO(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        pass
    def read(self, size=-1):
        return b'abc'
    def write(self, b):
        return len(b)
    def fileno(self):
        return -1
    def seekable(self):
        return False
    def readable(self):
        return True
    def writable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        pass
    def tell(self):
        return 0
    def close(self):
        pass
    def flush(self):
        pass
    def isatty(self):
        return False
    def readinto(self, b):
        return len(b)
    def truncate(self, size=None):
        return 0

r = TestRawIO()
r.readable()
r.writable()
r.seekable()
r.flush()
r.tell()
r.
