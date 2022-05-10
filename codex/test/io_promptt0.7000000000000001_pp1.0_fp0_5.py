import io
# Test io.RawIOBase
class MyIO(io.RawIOBase):

    def __init__(self):
        self.offset = 0
        self.v = memoryview(bytearray(b"1234567890"))

    def readinto(self, b):
        l = len(b)
        b[:l] = self.v[self.offset:self.offset+l]
        self.offset += l
        return l

print(io.RawIOBase.readinto)
# <slot wrapper 'readinto' of 'io.RawIOBase' objects>

i = MyIO()
print(i.readinto(bytearray(5)))
# 5
print(i.readinto(bytearray(5)))
# 5
print(i.readinto(bytearray(5)))
# 0
print(i.readinto(bytearray(5)))
# -1
print(i.readinto(bytearray(5)))
# -1
print(i.readinto(bytearray(5)))
# -1

# Test io.
