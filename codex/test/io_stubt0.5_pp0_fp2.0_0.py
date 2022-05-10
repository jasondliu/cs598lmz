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
view

# test for BufferedRWPair
# the BufferedRWPair is a simple wrapper around a pair of BufferedIOBase
# objects, so we test it here by testing that the wrapped objects are
# correctly called.

class Reader(io.BufferedIOBase):
    def __init__(self):
        self.readinto_called = False
        self.readable_called = False
    def readinto(self, buf):
        self.readinto_called = True
    def readable(self):
        self.readable_called = True
        return True

class Writer(io.BufferedIOBase):
    def __init__(self):
        self.write_called = False
        self.writable_called = False
    def write(self, buf):
        self.write_called = True
    def writable(self):
        self.writable_called = True
        return True

r = Reader()
w = Writer()
f = io.BufferedRWPair(r, w)
f.read(1)
f.write(b"1")
