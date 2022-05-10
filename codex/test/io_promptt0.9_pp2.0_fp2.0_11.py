import io
# Test io.RawIOBase.
r = io.RawIOBase()
try:
    r.tell()
except io.UnsupportedOperation:
    # True, assuming that io.RawIOBase.seek has not been overridden.
    pass

# Test io.BufferedIOBase.
b = io.BufferedIOBase()
