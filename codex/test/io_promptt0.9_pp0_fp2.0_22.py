import io
# Test io.RawIOBase
buf = io.BytesIO(b"\xe0\xe1\xe2\xe3") # A bytes-like object
buf.seek(0)
raw = io.RawIOBase(buf)
