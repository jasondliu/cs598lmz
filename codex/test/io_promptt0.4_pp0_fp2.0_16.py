import io
# Test io.RawIOBase

import _io

class C(io.RawIOBase):
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def fileno(self):
        return 42
    def isatty(self):
        return False
    def readinto(self, b):
        return 0
    def write(self, b):
        return 0
    def seek(self, offset, whence=0):
        return 0
    def tell(self):
        return 0
    def truncate(self, pos=None):
        return 0

class D(C):
    def read(self, n=-1):
        return b""
    def readall(self):
        return b""
    def read1(self, n=-1):
        return b""

class E(D):
    def close(self):
        pass

def test_io_rawiobase():
    c = C()
    assert c.readable()
    assert c.writable()
