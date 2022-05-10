import io
# Test io.RawIOBase
assert isinstance(io.DEFAULT_BUFFER_SIZE, int), repr(io.DEFAULT_BUFFER_SIZE)
r = io.RawIOBase()
try:
    r.read1()
    assert False, "This method should be abstract"
except io.UnsupportedOperation:
    pass
# Test io.BufferedIOBase
try:
    r.readinto1()
    assert False, "This method should be abstract"
except io.UnsupportedOperation:
    pass

io.BytesIO(b"hello").getvalue()

# Test io.IOBase
assert isinstance(io.SEEK_SET, int), repr(io.SEEK_SET)
assert isinstance(io.SEEK_CUR, int), repr(io.SEEK_CUR)
assert isinstance(io.SEEK_END, int), repr(io.SEEK_END)
# Test io.TextIOBase
try:
    r.read()
    assert False, "This method should be abstract"
except io.UnsupportedOperation:
    pass
try:
    r.read
