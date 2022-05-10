import io
# Test io.RawIOBase.readinto()
import sys

class ReadIntoTest:
    def __init__(self, fp):
        self.fp = fp

    def read(self, n):
        print("read({})".format(n))
        return self.fp.read(n)

    def readinto(self, b):
        print("readinto({})".format(b))
        data = self.fp.read(len(b))
        b[:len(data)] = data
        return len(data)

class TestRawIO(io.RawIOBase):
    def __init__(self, buf):
        self.buf = buf
        self.pos = 0
        self.size = len(buf)

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, pos, whence=0):
        self.check_closed()
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
