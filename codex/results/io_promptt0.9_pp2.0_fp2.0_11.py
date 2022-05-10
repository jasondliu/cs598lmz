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
try:
    b.peek(1)
except io.UnsupportedOperation:
    # True, assuming that io.BufferedIOBase.read has not been overridden.
    pass

# Test io.TextIOBase.
t = io.TextIOBase()
try:
    t.tell()
except io.UnsupportedOperation:
    # True, assuming that io.TextIOBase.seek has not been overridden.
    pass

# Test io.BytesIO.
f = io.BytesIO()
assert f.tell() == 0
f.close()
try:
    f.write(b'test')
except ValueError:
    # True, the BytesIO was closed.
    pass

# Test io.StringIO.
f = io.StringIO()

