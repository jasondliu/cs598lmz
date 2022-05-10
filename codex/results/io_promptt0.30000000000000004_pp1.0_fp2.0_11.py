import io
# Test io.RawIOBase.readinto()

import _io

class MyIO(io.RawIOBase):
    def readinto(self, b):
        b[0:4] = b"1234"
        return 4

buf = bytearray(5)
f = MyIO()
n = f.readinto(buf)
print(n, buf)
