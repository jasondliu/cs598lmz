import io
# Test io.RawIOBase
try:
    io.RawIOBase
except AttributeError:
    pass
else:
    class C(io.RawIOBase):
        def readinto(self, b):
            return super(C, self).readinto(b)
    c = C()
    c.readinto(bytearray(1))
