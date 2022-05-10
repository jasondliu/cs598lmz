import io
# Test io.RawIOBase
assert issubclass(io.RawIOBase, io.IOBase)
assert isinstance(io.BytesIO(), io.RawIOBase)

# Test io.BufferedIOBase
assert issubclass(io.BufferedIOBase, io.IOBase)
assert isinstance(io.BytesIO(), io.BufferedIOBase)

# Test io.TextIOBase
assert issubclass(io.TextIOBase, io.IOBase)
assert isinstance(io.StringIO(), io.TextIOBase)

# Test io.IOBase
assert hasattr(io.IOBase, 'close')
assert hasattr(io.IOBase, 'closed')
assert hasattr(io.IOBase, 'fileno')
assert hasattr(io.IOBase, 'flush')
assert hasattr(io.IOBase, 'isatty')
assert hasattr(io.IOBase, 'readable')
assert hasattr(io.IOBase, 'readline')
assert hasattr(io.IOBase, 'readlines')
assert hasattr(io.IOBase, 'seek')
assert hasattr(
