import io
# Test io.RawIOBase.readinto()

from test import support

# Issue #14982: On Windows, readinto() should return None if the
# underlying file descriptor is invalid.
support.requires('posix')

# Issue #13349: On Windows, readinto() should respect the 'b' flag.
support.requires('posix')

# Test that io.RawIOBase.readinto() works on a real file.

with open(support.TESTFN, 'wb') as f:
    f.write(b'abcdefghijklmnopqrstuvwxyz')

with open(support.TESTFN, 'rb') as f:
    buf = bytearray(b' ' * 26)
    n = f.readinto(buf)
    assert n == 26
    assert buf == b'abcdefghijklmnopqrstuvwxyz'

with open(support.TESTFN, 'rb') as f:
    buf = bytearray(b' ' * 26)
    n = f.readinto(memoryview(buf))
   
