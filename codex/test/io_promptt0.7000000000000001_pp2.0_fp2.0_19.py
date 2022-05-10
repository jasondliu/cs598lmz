import io
# Test io.RawIOBase

import io
import _pyio as pyio

class RawIOTest(io.RawIOBase):

    def read(self, n=-1):
        return b"foo"

    def readinto(self, b):
        b[:3] = b"foo"
        return 3

    def write(self, b):
        return len(b)

class RawIOTest2(io.RawIOBase):

    def readable(self):
        return True

    def seekable(self):
        return True

    def writable(self):
        return True

    def tell(self):
        return 42

    def read(self, n=-1):
        return b"foo"

    def readinto(self, b):
        b[:3] = b"foo"
        return 3

    def write(self, b):
        return len(b)

    def seek(self, pos, whence=0):
        pass

    def fileno(self):
        return 42

    def flush(self):
        pass

    def close(self):
        pass
