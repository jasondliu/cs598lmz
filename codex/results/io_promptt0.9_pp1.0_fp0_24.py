import io
# Test io.RawIOBase.readinto
b1 = bytearray(8)
io.BytesIO(b'0123456789').readinto(b1)
assert(b1 == b'01234567')

b1 = bytearray(1)
io.BytesIO(b'0123456789').readinto(b1)
assert(b1 == b'0')

b1 = bytearray(100)
io.BytesIO(b'').readinto(b1)
assert(b1 == b'')

# Test io.RawIOBase.readinto1
b1 = bytearray(8)
io.BytesIO(b'0123456789').readinto1(b1)
assert(b1 == b'01234567')

b1 = bytearray(1)
io.BytesIO(b'0123456789').readinto1(b1)
assert(b1 == b'0')

b1 = bytearray(100)
io.BytesIO().readinto1(b1)
assert(b
