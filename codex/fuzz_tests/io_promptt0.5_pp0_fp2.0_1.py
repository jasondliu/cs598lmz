import io
# Test io.RawIOBase.readall()

class MyRawIO(io.RawIOBase):
    def readall(self):
        return b"readall"
    def readable(self):
        return True

r = MyRawIO()
print(r.readall())
print(r.readall())

# Test io.RawIOBase.readinto()

class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        b[:] = b"readinto"
        return 8
    def readable(self):
        return True

r = MyRawIO()
buf = bytearray(10)
print(r.readinto(buf))
print(buf)
print(r.readinto(buf))
print(buf)

# Test io.RawIOBase.readinto() with a read-only buffer

class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        b[:] = b"readinto"
        return 8
    def readable(self):
        return True

r = MyRawIO()

