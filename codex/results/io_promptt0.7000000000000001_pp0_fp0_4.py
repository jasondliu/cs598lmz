import io
# Test io.RawIOBase.readinto()
assert isinstance(io.FileIO(__file__, 'r').readinto(bytearray()), int)
# Test io.BufferedIOBase.readinto()
assert isinstance(io.BufferedReader(io.FileIO(__file__, 'r')).readinto(bytearray()), int)
# Test io.TextIOBase.readinto()
assert isinstance(io.TextIOWrapper(io.FileIO(__file__, 'r'), encoding='utf-8').readinto(bytearray()), int)

# Test that io.BytesIO.write() and io.BytesIO.readinto() can handle bytearrays
b = io.BytesIO()
b.write(bytearray(b'foo'))
assert b.getvalue() == b'foo'
b = io.BytesIO()
assert b.readinto(bytearray(3)) == 0
b.write(bytearray(b'foo'))
assert b.getvalue() == b'foo'
b.seek(0)

