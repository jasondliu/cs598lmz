import io
# Test io.RawIOBase.readinto()

import _io

# Issue #17649: check that readinto() returns None
class MyRawIO(_io.RawIOBase):
    def readinto(self, b):
        return None

MyRawIO().readinto(bytearray(1))

# Issue #17649: check that readinto() raises TypeError
class MyRawIO(_io.RawIOBase):
    def readinto(self, b):
        return 1

try:
    MyRawIO().readinto(bytearray(1))
except TypeError:
    pass
else:
    raise Exception("expected TypeError")

# Issue #17649: check that readinto() raises TypeError
class MyRawIO(_io.RawIOBase):
    def readinto(self, b):
        return -1

try:
    MyRawIO().readinto(bytearray(1))
except ValueError:
    pass
else:
    raise Exception("expected ValueError")

# Issue #17649: check that readinto() raises TypeError
class MyRawIO(_io.
