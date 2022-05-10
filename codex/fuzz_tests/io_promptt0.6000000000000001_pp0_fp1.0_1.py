import io
# Test io.RawIOBase
assert issubclass(io.RawIOBase, io.IOBase)
# Test io.BufferedIOBase
assert issubclass(io.BufferedIOBase, io.IOBase)
# Test io.TextIOBase
assert issubclass(io.TextIOBase, io.IOBase)

# Test io.FileIO
f = io.FileIO("io.py")
assert issubclass(type(f), io.RawIOBase)
assert issubclass(type(f), io.FileIO)
assert issubclass(type(f), io.BufferedIOBase)
f.close()

# Test io.BytesIO
f = io.BytesIO()
assert issubclass(type(f), io.BufferedIOBase)
assert issubclass(type(f), io.BytesIO)
assert issubclass(type(f), io.RawIOBase)
f.close()

# Test io.StringIO
f = io.StringIO()
assert issubclass(type(f), io.BufferedIOBase)
assert issubclass(type(f), io
