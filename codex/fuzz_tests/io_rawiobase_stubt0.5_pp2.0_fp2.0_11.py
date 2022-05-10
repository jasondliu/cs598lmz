import io
class File(io.RawIOBase):
    def read(self, n = -1):
        return b'123'

f = File()
print(f.read())

class File(io.RawIOBase):
    def read(self, n = -1):
        return b'123'
    def readinto(self, b):
        # b is a bytearray
        data = self.read()
        n = len(b)
        view = memoryview(b).cast('B')
        view[:len(data)] = data
        return len(data)

f = File()
print(f.readinto(bytearray(5)))
# 3
print(f.readinto(bytearray(5)))
# 0

import io
class File(io.RawIOBase):
    def read(self, n = -1):
        return b'123'
    def readinto(self, b):
        # b is a bytearray
        data = self.read()
        n = len(b)
        view = memoryview(b).cast('B')
        view
