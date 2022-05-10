import io
# Test io.RawIOBase

import _io

fp = _io.BytesIO()
fp.write(b'1234567890')
fp.seek(0)

# Test readinto
buf = bytearray(5)
n = fp.readinto(buf)
assert n == 5
assert buf == b'12345'

# Test readall
