import io
# Test io.RawIOBase
try:
    io.RawIOBase
except NameError:
    print("SKIP")
    raise SystemExit

import io

class MyRawIO(io.RawIOBase):
    def readinto(self, buf):
        return 0

try:
    io.RawIOBase()
except TypeError:
    print("TypeError")
