import io
# Test io.RawIOBase
import io
import _io

class C(io.RawIOBase):
    def readinto(self, b):
        return 0

buf = bytearray(100)
C().readinto(buf)

try:
    C().readinto(b'123')
except TypeError:
    print("TypeError")

try:
    C().readinto(memoryview(b'123'))
except TypeError:
    print("TypeError")

# Test io.BufferedIOBase
import io

class C(io.BufferedIOBase):
    def readinto(self, b):
        return 0

buf = bytearray(100)
C().readinto(buf)

try:
    C().readinto(b'123')
except TypeError:
    print("TypeError")

try:
    C().readinto(memoryview(b'123'))
except TypeError:
    print("TypeError")
