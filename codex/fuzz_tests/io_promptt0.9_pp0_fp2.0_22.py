import io
# Test io.RawIOBase
buf = io.BytesIO(b"\xe0\xe1\xe2\xe3") # A bytes-like object
buf.seek(0)
raw = io.RawIOBase(buf)
data = raw.read(2) # bytes object returned
data
data = raw.read(1)
raw.seek(3)
data = raw.read(1)
data
# Test io.BufferedReader
buf.seek(0)
buf.read(2)
buf = io.BufferedReader(buf)
buf.read(2)
buf.read(8)
# buf.seek(3)
# buf.read(2)
# buf.read(1)
# buf
buf.closed
buf.seekable()
buf = io.BufferedReader(io.BytesIO(b"\x00\x01\x02\x03"))
buf.seek(2)
buf.read(2)
buf.seek(0)
buf.read(2)

import sys
print(sys.getrefcount('1'))
import pickle # Uses __reduce
