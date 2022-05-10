import io
# Test io.RawIOBase

import _io

class TestRawIOBase(_io.RawIOBase):
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def readinto(self, b):
        b[:3] = b"foo"
        return 3
    def write(self, b):
        pass
    def seek(self, pos, whence=0):
        pass
    def tell(self):
        return 0
    def close(self):
        pass

class TestRawIO(_io.RawIOBase):
    def __init__(self):
        self.read_history = []
        self.write_history = []
        self.seek_history = []
        self.tell_history = []
        self.closed = False
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def readinto(self, b):
        self.read_history.append(b)
        b[
