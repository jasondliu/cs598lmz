import io
# Test io.RawIOBase.readinto()

import _io

class MyRawIO(_io.RawIOBase):
    def readinto(self, buf):
        return buf.__reduce__()[1][0]

buf = bytearray(5)
print(MyRawIO().readinto(buf))
