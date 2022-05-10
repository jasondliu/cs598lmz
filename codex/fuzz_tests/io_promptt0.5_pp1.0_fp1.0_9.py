import io
# Test io.RawIOBase

import _io

# Issue #17774: io.RawIOBase.read() should return an empty bytes object
# when passed a zero length argument.
r = _io.BytesIO(b"abc")
assert r.read(0) == b""

# Issue #17774: io.RawIOBase.readall() should return an empty bytes object
# when passed a zero length argument.
r = _io.BytesIO(b"abc")
assert r.readall(0) == b""

# Issue #17774: io.RawIOBase.readinto() should return zero when passed
# a zero length argument.
r = _io.BytesIO(b"abc")
b = bytearray(1)
assert r.readinto(b, 0) == 0

# Issue #17774: io.RawIOBase.readinto() should return zero when passed
# a zero length argument.
r = _io.BytesIO(b"abc")
b = bytearray(1)
assert r.readinto(b, 0) == 0

# Issue #17774:
