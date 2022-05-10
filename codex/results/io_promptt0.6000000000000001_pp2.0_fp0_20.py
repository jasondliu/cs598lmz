import io
# Test io.RawIOBase
with io.BytesIO() as buf:
    buf.raw

# Test io.BufferedIOBase
with io.BytesIO() as buf:
    buf.buffer

# Test io.TextIOBase
with io.StringIO() as buf:
    buf.buffer

# Test io.RawIOBase
with io.FileIO(__file__) as f:
    f.raw

# Test io.BufferedIOBase
with io.FileIO(__file__) as f:
    f.buffer

# Test io.TextIOBase
with io.FileIO(__file__) as f:
    f.buffer

# Test io.RawIOBase
with io.StringIO() as buf:
    buf.raw

# Test io.BufferedIOBase
with io.StringIO() as buf:
    buf.buffer

# Test io.TextIOBase
with io.StringIO() as buf:
    buf.buffer


# Testing for issue #39
class MyRawIO(io.RawIOBase):
    def readinto(self, b):
        return
