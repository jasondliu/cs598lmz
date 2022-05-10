import io
# Test io.RawIOBase by using a raw string
s = io.BytesIO(b'abc')
s.read()
# io.RawIOBase.read() calls io.RawIOBase.readinto()
s.readinto(bytearray(10))
# Test io.RawIOBase by using a bytearray
b = bytearray(b'abc')
s = io.BytesIO(b)
s.read()
# Test io.RawIOBase by using an array.array
