import io
# Test io.RawIOBase.readinto() and io.RawIOBase.write()

import _io

# Test readinto()
try:
    _io.RawIOBase().readinto(bytearray())
except AttributeError:
    pass
else:
    print('AttributeError expected')

try:
    _io.RawIOBase().readinto(memoryview(bytearray(1)))
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test write()
try:
    _io.RawIOBase().write(bytes())
except AttributeError:
    pass
else:
    print('AttributeError expected')

# io.RawIOBase has a sane default for readinto which checks for
# readable, seekable, and writable.
try:
    class MyRawIO(_io.RawIOBase):
        def readinto(self, b):
            return _io.RawIOBase.readinto(self, b)
except AttributeError:
    pass
else:
    print('AttributeError expected')

try:
    class MyRawIO
