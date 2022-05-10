import io
# Test io.RawIOBase.readinto()
#
# This feature is not yet supported by the micropython-lib implementation
# of io.IOBase
#

print("Test io.RawIOBase.readinto()")

class TestRawIO(io.RawIOBase):
    def __init__(self):
        self.pos = 0
        self.buf = b'abcdefghij'
    def readable(self):
        return True
    def readinto(self, b):
        l = len(b)
        if self.pos >= len(self.buf):
            return None
        if self.pos + l > len(self.buf):
            l = len(self.buf) - self.pos
        b[:l] = self.buf[self.pos:self.pos+l]
        self.pos += l
        return l

r = TestRawIO()

print("---readinto(bytearray)")
s = bytearray(5)
print(r.readinto(s))
print(s)

print("---readinto(memoryview)")
