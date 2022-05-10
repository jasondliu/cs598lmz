import io
# Test io.RawIOBase
with io.BytesIO() as f:
    isinstance(f, io.RawIOBase)
