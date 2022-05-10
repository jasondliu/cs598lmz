import io
# Test io.RawIOBase
assert issubclass(io.RawIOBase, io.IOBase)
# Test io.BufferedIOBase
assert issubclass(io.BufferedIOBase, io.IOBase)
# Test io.TextIOBase
assert issubclass(io.TextIOBase, io.IOBase)

# Test io.FileIO
assert issubclass(io.FileIO, io.RawIOBase)
assert issubclass(io.FileIO, io.BufferedIOBase)

# Test io.BufferedRandom
assert issubclass(io.BufferedRandom, io.FileIO)
assert issubclass(io.BufferedRandom, io.BufferedIOBase)
assert issubclass(io.BufferedRandom, io.RawIOBase)

# Test io.TextIOWrapper
assert issubclass(io.TextIOWrapper, io.TextIOBase)
assert issubclass(io.TextIOWrapper, io.BufferedIOBase)

# Test io.StringIO
assert issubclass(io.StringIO, io.TextIOBase)
assert iss
