import io
# Test io.RawIOBase
assert issubclass(io.RawIOBase, io.IOBase)

# Test io.BufferedIOBase
assert issubclass(io.BufferedIOBase, io.RawIOBase)

assert issubclass(io.BufferedWriter, io.BufferedIOBase)
assert issubclass(io.BufferedReader, io.BufferedIOBase)
assert issubclass(io.BufferedRWPair, io.BufferedIOBase)

assert issubclass(io.BufferedRandom, io.BufferedIOBase)
assert issubclass(io.BufferedRandom, io.RawIOBase)

assert issubclass(io.TextIOBase, io.IOBase)
assert issubclass(io.TextIOWrapper, io.TextIOBase)
