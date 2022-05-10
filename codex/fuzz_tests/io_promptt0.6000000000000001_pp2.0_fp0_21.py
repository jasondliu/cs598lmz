import io
# Test io.RawIOBase

# test readall
r = io.BytesIO(b'abc')
assert r.readall() == b'abc'
r = io.BytesIO(b'')
assert r.readall() == b''

# test readinto
b = bytearray(b' '*10)
n = r.readinto(b)
assert n == 0
assert r.readinto(b) == 0
assert b == b' '*10

b = bytearray(b' '*10)
r = io.BytesIO(b'abcdefgh')
n = r.readinto(b)
assert n == 8
assert b == b'abcdefgh' + b' '*2

b = bytearray(b' '*10)
r = io.BytesIO(b'abcdefgh')
n = r.readinto(b, 2)
assert n == 8
assert b == b' '*2 + b'abcdefgh' + b' '*2

b = bytearray(b' '*10)
r = io.Bytes
