import io
# Test io.RawIOBase

import _io

class MyRawIO(_io.RawIOBase):
    def read(self, n=-1):
        return b"xyz"

try:
    MyRawIO().readinto(bytearray())
except TypeError:
    print("SKIP")
    raise SystemExit

# Test io.BufferedIOBase

class MyBufferedIO(_io.BufferedIOBase):
    def read(self, n=-1):
        return b"xyz"

try:
    MyBufferedIO().readinto(bytearray())
except TypeError:
    print("SKIP")
    raise SystemExit

# Test io.TextIOBase

class MyTextIO(_io.TextIOBase):
    def read(self, n=-1):
        return "xyz"

try:
    MyTextIO().readinto(bytearray())
except TypeError:
    print("SKIP")
    raise SystemExit
