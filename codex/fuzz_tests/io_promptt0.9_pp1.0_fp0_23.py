import io
# Test io.RawIOBase
with io.BytesIO() as f:
    isinstance(f, io.RawIOBase)
    f.fileno()

# Test io.BufferedIOBase
with io.BufferedReader(io.BytesIO()) as f:
    isinstance(f, io.BufferedIOBase)
    isinstance(f, io.RawIOBase)

# Test io.TextIOBase
with io.StringIO() as f:
    isinstance(f, io.TextIOBase)
    isinstance(f, io.IOBase)
    isinstance(f, io.RawIOBase)

with io.StringIO(u"test") as f:
    isinstance(f.read(1), str)
    f.seek(0)
    isinstance(f.readline(), str)

with io.TextIOWrapper(io.BytesIO(), encoding="ascii", errors="strict") as f:
    isinstance(f, io.TextIOBase)
    isinstance(f, io.BufferedIOBase)
    isinstance(f, io.Raw
