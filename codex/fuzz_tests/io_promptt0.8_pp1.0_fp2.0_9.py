import io
# Test io.RawIOBase as a base class for raw I/O
class MultipleRawIOBase(io.RawIOBase):
    def read(self, size=-1):
        if size == 3:
            return b'\x01\x02\x03'
        return super().read(size)
    def readall(self):
        return b'\x01\x02'
    def seek(self, offset, whence=io.SEEK_SET):
        return super().seek(offset, whence)
    def seekable(self):
        return True
    def fileno(self):
        return super().fileno()
    def tell(self):
        return super().tell()
    def readable(self):
        return True
    def readinto(self, b):
        b[:2] = b'\x01\x02'
        return 2

class MyRawIO(MultipleRawIOBase):
    def writable(self):
        return True
    def write(self, b):
        self.b = b
        return len(b)
    def flush(self):
        pass

