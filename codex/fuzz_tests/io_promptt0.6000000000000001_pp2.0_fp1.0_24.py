import io
# Test io.RawIOBase
assert issubclass(io.RawIOBase, io.IOBase)
assert issubclass(io.RawIOBase, io.BufferedIOBase)
assert issubclass(io.RawIOBase, io.RawIOBase)
# Test io.BufferedIOBase
assert issubclass(io.BufferedIOBase, io.IOBase)
assert issubclass(io.BufferedIOBase, io.BufferedIOBase)
assert not issubclass(io.BufferedIOBase, io.RawIOBase)
# Test io.TextIOBase
assert issubclass(io.TextIOBase, io.IOBase)
assert issubclass(io.TextIOBase, io.TextIOBase)
assert not issubclass(io.TextIOBase, io.RawIOBase)
assert not issubclass(io.TextIOBase, io.BufferedIOBase)
# Test io.FileIO
assert issubclass(io.FileIO, io.IOBase)
assert issubclass(io.FileIO, io.RawIOBase)
assert issubclass(io.FileIO, io
