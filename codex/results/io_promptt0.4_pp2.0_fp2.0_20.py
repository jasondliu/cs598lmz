import io
# Test io.RawIOBase

import _io

class MyRawIO(_io.RawIOBase):
    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        b[:] = b'a' * len(b)
        return len(b)

    def write(self, b):
        return len(b)

    def seek(self, pos, whence=0):
        return 0

    def tell(self):
        return 0

class MyRawIO2(_io.RawIOBase):
    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        b[:] = b'a' * len(b)
        return len(b)

    def write(self, b):
        return len(b)

    def seek(self, pos, whence=0):
        return 0

    def tell(self):
        return 0


