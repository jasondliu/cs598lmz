import io
# Test io.RawIOBase.read()
class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        n = len(b)
        b[:] = bytearray(n)
        return n
    def readable(self):
        return True
r = MyRawIO()
b = bytearray(5)
r.readinto(b)
b

# Test io.RawIOBase.readinto()
class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        n = len(b)
        b[:] = bytearray(n)
        return n
    def readable(self):
        return True
r = MyRawIO()
b = bytearray(5)
r.readinto(b)
b

# Test io.RawIOBase.seek()
class MyRawIO(io.RawIOBase):
    def seek(self, pos, whence=0):
        if whence == 0:
            self.pos = pos
        elif whence == 1:
            self.pos += pos
        el
