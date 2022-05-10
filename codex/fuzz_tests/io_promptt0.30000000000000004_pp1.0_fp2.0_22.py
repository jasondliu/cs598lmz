import io
# Test io.RawIOBase.readinto()

import _io

class MyRawIO(_io.RawIOBase):
    def readinto(self, b):
        b[0] = ord('x')
        return 1

def main():
    b = bytearray(10)
    r = MyRawIO()
    n = r.readinto(b)
    assert n == 1
    assert b[0] == ord('x')
    assert b[1] == 0
    n = r.readinto(b)
    assert n == 0

main()
