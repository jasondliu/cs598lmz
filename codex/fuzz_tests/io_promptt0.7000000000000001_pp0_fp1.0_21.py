import io
# Test io.RawIOBase
assert issubclass(io.RawIOBase, object)
assert issubclass(io.RawIOBase, io.IOBase)
assert hasattr(io.RawIOBase, 'read')
assert hasattr(io.RawIOBase, 'readinto')
assert hasattr(io.RawIOBase, 'write')
assert hasattr(io.RawIOBase, 'fileno')
assert hasattr(io.RawIOBase, 'seek')
assert hasattr(io.RawIOBase, 'tell')
assert hasattr(io.RawIOBase, 'truncate')
# Test io.FileIO
assert issubclass(io.FileIO, object)
assert issubclass(io.FileIO, io.RawIOBase)
assert hasattr(io.FileIO, '__init__')
assert hasattr(io.FileIO, 'close')
assert hasattr(io.FileIO, 'closed')
assert hasattr(io.FileIO, 'flush')
assert hasattr(io.FileIO, 'fileno')
assert hasattr(io.FileIO, 'mode')
assert hasattr
