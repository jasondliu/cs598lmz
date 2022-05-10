import io
# Test io.RawIOBase.read()

# This test checks that io.RawIOBase.read() returns an empty bytes
# object (not None) when the stream is at EOF, and that it returns
# None when the maximum length is zero.

import _io

class TestRawIO(_io.RawIOBase):
    def read(self, n=-1):
        return b''

try:
    TestRawIO().read()
except TypeError:
    print('SKIP')
    raise SystemExit

t = TestRawIO()
print(t.read() == b'')
print(t.read() == b'')
print(t.read(0) == b'')

# Check that the max length argument can be omitted
t.read()
t.read()

# Check that the max length argument can be zero
t.read(0)
t.read(0)

# Check that the max length argument can be greater than zero
t.read(10)

# Check that the max length argument can be omitted
# when a non-zero length has previously been given
t.read(
