import io
# Test io.RawIOBase
assert issubclass(io.RawIOBase, io.IOBase)
# Test io.BufferedIOBase
assert issubclass(io.BufferedIOBase, io.IOBase)
# Test io.TextIOBase
assert issubclass(io.TextIOBase, io.IOBase)

# Test io.FileIO
