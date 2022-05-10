import io
# Test io.RawIOBase
print(issubclass(io.RawIOBase, io.IOBase))

# Test io.BufferedIOBase
print(issubclass(io.BufferedIOBase, io.IOBase))

# Test io.TextIOBase
print(issubclass(io.TextIOBase, io.IOBase))

# Test io.BytesIO
print(issubclass(io.BytesIO, io.RawIOBase))
print(issubclass(io.BytesIO, io.BufferedIOBase))
print(issubclass(io.BytesIO, io.IOBase))

# Test io.StringIO
print(issubclass(io.StringIO, io.TextIOBase))
print(issubclass(io.StringIO, io.IOBase))

# Test io.BufferedReader
print(issubclass(io.BufferedReader, io.RawIOBase))
print(issubclass(io.BufferedReader, io.BufferedIOBase))
print(issubclass(io.BufferedReader, io.IOBase))

# Test io.BufferedWriter

