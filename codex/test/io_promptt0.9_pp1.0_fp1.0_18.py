import io
# Test io.RawIOBase handling

with io.BytesIO(b"foo") as fobj:
    o = io.RawIOBase()
