import io
# Test io.RawIOBase
assert isinstance(io.DEFAULT_BUFFER_SIZE, int), repr(io.DEFAULT_BUFFER_SIZE)
r = io.RawIOBase()
