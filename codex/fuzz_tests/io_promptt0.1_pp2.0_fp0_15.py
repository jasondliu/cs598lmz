import io
# Test io.RawIOBase

import _io

class MyRawIO(_io.RawIOBase):
    def readinto(self, b):
        b[:3] = b"foo"
        return 3

try:
    MyRawIO().readinto(bytearray(2))
except TypeError:
    print("SKIP")
    raise SystemExit

# Test io.BufferedIOBase

class MyBufferedIO(_io.BufferedIOBase):
    def __init__(self, raw):
        self.raw = raw

    def readinto(self, b):
        return self.raw.readinto(b)

try:
    MyBufferedIO(MyRawIO()).readinto(bytearray(2))
except TypeError:
    print("SKIP")
    raise SystemExit

# Test io.TextIOBase

class MyTextIO(_io.TextIOBase):
    def readinto(self, b):
        b[:3] = "foo"
        return 3

try:
    MyTextIO().readinto(bytearray(2
