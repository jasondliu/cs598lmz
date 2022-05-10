import io
# Test io.RawIOBase
with io.BytesIO() as f:
    f.write(b"foo")
    f.seek(0)
    f.readline()
# Test io.BufferedIOBase
with io.BytesIO() as f:
    f.write(b"foo")
    f.seek(0)
    f.read()
    f.read1()
# Test io.TextIOBase
with io.StringIO() as f:
    f.seek(0)
    f.readline()
# Test io.IOBase
with io.StringIO() as f:
    f.seek(0)
    f.readline()
# Test io.RawIOBase
with io.BytesIO() as f:
    f.write(b"foo")
    f.seek(0)
    f.readline()
# Test io.BufferedIOBase
with io.BytesIO() as f:
    f.write(b"foo")
    f.seek(0)
    f.read()
    f.read1()
# Test io.TextIOBase
