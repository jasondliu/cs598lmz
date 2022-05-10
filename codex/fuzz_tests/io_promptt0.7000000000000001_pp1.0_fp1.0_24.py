import io
# Test io.RawIOBase
assert issubclass(io.RawIOBase, io.IOBase)
assert issubclass(io.RawIOBase, io.FileIO)
assert issubclass(io.RawIOBase, io.BufferedIOBase)
assert issubclass(io.RawIOBase, io.RawIO)
# Test io.BufferedIOBase
assert issubclass(io.BufferedIOBase, io.IOBase)
assert issubclass(io.BufferedIOBase, io.FileIO)
assert issubclass(io.BufferedIOBase, io.BufferedIO)
assert issubclass(io.BufferedIOBase, io.BufferedIOBase)
# Test io.FileIO
assert issubclass(io.FileIO, io.BufferedIO)
assert issubclass(io.FileIO, io.FileIO)
# Test io.BytesIO
assert issubclass(io.BytesIO, io.BufferedIO)
assert issubclass(io.BytesIO, io.BytesIO)
assert issubclass(io.BytesIO, io.BufferedIOBase)
# Test
