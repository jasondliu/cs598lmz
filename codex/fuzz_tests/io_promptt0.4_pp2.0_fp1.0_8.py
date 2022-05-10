import io
# Test io.RawIOBase
with io.BytesIO() as f:
    f.write(b"hello")
    s = f.getvalue()
    assert s == b"hello"

with io.BytesIO(b"hello") as f:
    s = f.read()
    assert s == b"hello"

with io.BytesIO(b"hello") as f:
    s = f.read(2)
    assert s == b"he"
    s = f.read(2)
    assert s == b"ll"
    s = f.read(2)
    assert s == b"o"
    s = f.read(2)
    assert s == b""

with io.BytesIO(b"hello") as f:
    s = f.readline()
    assert s == b"hello"

with io.BytesIO(b"hello\nworld") as f:
    s = f.readline()
    assert s == b"hello\n"
    s = f.readline()
    assert s == b"world"

with io.BytesIO
