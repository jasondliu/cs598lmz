import io
# Test io.RawIOBase.readall()

raw = io.RawIOBase()
raw.mode = 'rb'

# readall() may return less than the requested number of bytes
# if the underlying raw stream is not seekable.
# That's why we use a StringIO instead of a BytesIO.
raw._readall = lambda n: io.BytesIO(b'a' * n).read(n)

data = b'x' * (io.DEFAULT_BUFFER_SIZE * 2)

# Test readall() on a non-seekable raw stream
raw.seekable = lambda: False
