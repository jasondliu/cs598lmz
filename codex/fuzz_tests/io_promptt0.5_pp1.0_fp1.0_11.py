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
buf = fp.readall()
assert buf == b'67890'

# Test read
buf = fp.read(5)
assert buf == b''

buf = fp.read(5)
assert buf == b''

# Test read1
buf = fp.read1(5)
assert buf == b''

# Test seek
fp.seek(0)
buf = fp.read(5)
assert buf == b'12345'

fp.seek(6)
buf = fp.read(5)
assert buf == b'67890'

fp.seek(-5, 2)
buf = fp.read(5)
assert buf == b'67890'

fp.seek(0,
