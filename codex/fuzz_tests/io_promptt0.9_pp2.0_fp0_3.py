import io
# Test io.RawIOBase
print(issubclass(io.RawIOBase, object))

from io import RawIOBase
print(issubclass(RawIOBase, object))
