import io
# Test io.RawIOBase.readinto()

import _io

class MyIO(_io.RawIOBase):
    def readinto(self, b):
        b[0:4] = b"1234"
        return 4

io.BytesIO(b"").readinto(bytearray(4))
MyIO().readinto(bytearray(4))
