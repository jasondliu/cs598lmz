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
print(raw.readall() == data)

# Test readall() on a seekable raw stream
raw.seekable = lambda: True
print(raw.readall() == data)


class MyRawIOBase(io.RawIOBase):
    def readall(self):
        return super().readall() + b'a' * 5

raw = MyRawIOBase()
raw.mode = 'rb'
raw.seekable = lambda: True
data = b'x' * (io.
