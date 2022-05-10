import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
print(view)
del view

# Issue #18895: test that __del__ is called when an I/O operation raises an
# exception in C code.

from test.support import verbose, _2G, _4G

class DelException(Exception):
    pass

class DelIO(io.IOBase):
    def __init__(self):
        self.closed = False
    def readinto(self, buf):
        if verbose:
            print("readinto")
        raise DelException
    def writable(self):
        if verbose:
            print("writable")
        raise DelException
    def close(self):
        if verbose:
            print("close")
        self.closed = True
    def __del__(self):
        if verbose:
            print("__del__", self.closed)
        if not self.closed:
            raise RuntimeError

del f
del b
for bufsize in range(1, 10):
    if verbose:
        print("bufsize =", bufsize)
    f = DelIO()
