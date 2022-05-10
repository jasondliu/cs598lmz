import io
# Test io.RawIOBase.readinto()

# Test readinto() with normal buffer
with open(io.DEFAULT_BUFFER_SIZE * b'a', 'rb') as f:
    buf = bytearray(io.DEFAULT_BUFFER_SIZE)
    n = f.readinto(buf)
    assert n == io.DEFAULT_BUFFER_SIZE
    assert buf == bytearray(io.DEFAULT_BUFFER_SIZE * b'a')

# Test readinto() with memoryview
with open(io.DEFAULT_BUFFER_SIZE * b'a', 'rb') as f:
    buf = bytearray(io.DEFAULT_BUFFER_SIZE)
    n = f.readinto(memoryview(buf))
    assert n == io.DEFAULT_BUFFER_SIZE
    assert buf == bytearray(io.DEFAULT_BUFFER_SIZE * b'a')

# Test readinto() with bytearray
with open(io.DEFAULT_BUFFER_SIZE * b'a', 'rb') as f:
    buf = bytearray
