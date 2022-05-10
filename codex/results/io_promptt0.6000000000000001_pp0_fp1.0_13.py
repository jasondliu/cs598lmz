import io
# Test io.RawIOBase.readinto() with a mutable buffer.
import _io

class MutableBytesIO(_io.RawIOBase):

    def __init__(self, value):
        self.buf = bytearray(value)

    def readable(self):
        return True

    def seekable(self):
        return True

    def writeable(self):
        return False

    def seek(self, offset, whence=0):
        if whence == 0:
            self.pos = offset
        elif whence == 1:
            self.pos += offset
        elif whence == 2:
            self.pos = len(self.buf) + offset
        else:
            raise ValueError('invalid whence')
        return self.pos

    def tell(self):
        return self.pos

    def readinto(self, b):
        n = len(b)
        if self.pos >= len(self.buf):
            return 0
        if n > len(self.buf) - self.pos:
            n = len(self.buf) - self.pos
        b[:n
