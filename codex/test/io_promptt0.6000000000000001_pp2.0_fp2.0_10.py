import io
# Test io.RawIOBase.readall(), which returns the remaining bytes from the stream.

stream = io.BytesIO(b'a' * 10)
