import io
# Test io.RawIOBase.readinto()

# Test basic readinto.
r = io.BytesIO( b"xyz\n" )
b = bytearray( 4 )
assert r.readinto( b ) == 4
