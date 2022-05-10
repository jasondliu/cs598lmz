import io
# Test io.RawIOBase.readinto()

# Test basic readinto.
r = io.BytesIO( b"xyz\n" )
b = bytearray( 4 )
assert r.readinto( b ) == 4
assert b == bytearray( b"xyz\n\0" )

# Test readinto with offset.
r = io.BytesIO( b"xyz\n" )
b = bytearray( 4 )
assert r.readinto( b, 1 ) == 3
assert b == bytearray( b"\0xyz\n" )

# Test readinto with negative offset.
r = io.BytesIO( b"xyz\n" )
b = bytearray( 4 )
try:
    r.readinto( b, -1 )
except ValueError:
    pass
else:
    assert False, "negative offset didn't raise ValueError"

# Test readinto with offset past end of buffer.
r = io.BytesIO( b"xyz\n" )
b = bytearray( 4 )
try:
   
