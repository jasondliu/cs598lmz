import io
# Test io.RawIOBase
n = io.BytesIO()
t = type(n)
print(t)

print(issubclass(t, io.RawIOBase))

print(issubclass(t, io.IOBase))

print(isinstance(n, io.RawIOBase))

print(isinstance(n, io.IOBase))

print(hasattr(n, 'close'))

print(hasattr(n, 'fileno'))

print(hasattr(n, 'isatty'))

print(hasattr(n, 'readable'))

print(hasattr(n, 'seekable'))

# Test io.BufferedIOBase

# Issue #10763: io.BufferedIOBase is not a new-style class

print(issubclass(t, io.BufferedIOBase))

print(isinstance(n, io.BufferedIOBase))

print(hasattr(n, 'read'))

print(hasattr(n, 'read1'))

# Test io.TextIOBase

# Issue #10
