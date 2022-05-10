import io
# Test io.RawIOBase.read() method

import _io

# Create a test raw stream
class MyRawIO(_io.RawIOBase):
    def readinto(self, b):
        b[0] = ord('a')
        return 1

try:
    MyRawIO().read()
except TypeError:
    print("SKIP")
    raise SystemExit

print("pass")
