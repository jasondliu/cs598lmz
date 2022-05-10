import io
class File(io.RawIOBase):
    def read(self, size=-1):
        return self.readinto(bytearray(size))
    def readinto(self, b):
        n = len(b)
        if n == 0:
            return 0
        if not hasattr(self, 'buf'):
            self.buf = bytearray(b'\x00' * n)
        else:
            self.buf = self.buf[n:] + bytearray(b'\x00' * n)
        b[:] = self.buf
        return len(b)
    def readable(self):
        return True
    def seekable(self):
        return True
    def writable(self):
        return False
    def seek(self, offset, whence=0):
        if whence == 0:
            self.buf = self.buf[offset:]
        elif whence == 1:
            self.buf = self.buf[offset:] + bytearray(b'\x00' * offset)
        else:
            raise ValueError('invalid whence (%r, should be 0
