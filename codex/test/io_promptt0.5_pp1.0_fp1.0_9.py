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
