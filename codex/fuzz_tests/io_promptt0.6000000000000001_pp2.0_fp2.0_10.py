import io
# Test io.RawIOBase.readall(), which returns the remaining bytes from the stream.

stream = io.BytesIO(b'a' * 10)
assert stream.readall() == b'a' * 10
assert stream.readall() == b''
# Test io.RawIOBase.readinto(), which fills a buffer with the stream contents.

buf = bytearray(10)

stream = io.BytesIO(b'a' * 10)
assert stream.readinto(buf) == 10
assert buf == b'a' * 10

# Test that the buffer is only partially filled.
stream = io.BytesIO(b'a' * 9)
assert stream.readinto(buf) == 9
assert buf == b'a' * 9 + b'\x00'
# Test that io.BytesIO.readinto() raises ValueError when the buffer is too small.

buf = bytearray(10)

stream = io.BytesIO(b'a' * 11)
with pytest.raises(ValueError):
    stream.readinto(buf)
# Test io.RawIOBase.
