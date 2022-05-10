import io
# Test io.RawIOBase.
assert issubclass(io.RawIOBase, io.IOBase)
assert issubclass(io.RawIOBase, object)

