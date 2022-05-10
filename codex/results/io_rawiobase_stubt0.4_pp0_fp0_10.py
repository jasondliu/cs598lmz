import io
class File(io.RawIOBase):
    def __init__(self):
        self.closed = False
        self.pos = 0
        self.buffer = bytearray(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F')
        self.len = len(self.buffer)
    def tell(self):
        return self.pos
    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        elif whence == 2:
            self.pos = self.len + pos
        else:
            raise ValueError('whence must be 0, 1 or 2')
        return self.pos
    def readinto(self, b):
        l = len(b)
        if self.pos + l > self.len:
            l = self.len - self.pos
            b = memoryview(b)[:l
