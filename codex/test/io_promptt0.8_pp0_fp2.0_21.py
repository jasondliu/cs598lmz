import io
# Test io.RawIOBase
print(isinstance(io.RawIOBase(), io.RawIOBase))
print(issubclass(io.RawIOBase, io.IOBase))

# Test io.BufferedIOBase
print(isinstance(io.BufferedIOBase(), io.BufferedIOBase))
print(issubclass(io.BufferedIOBase, io.RawIOBase))

# Test io.TextIOBase
print(isinstance(io.TextIOBase(), io.TextIOBase))
print(issubclass(io.TextIOBase, io.RawIOBase))

# Test io.BytesIO
print(isinstance(io.BytesIO(), io.BytesIO))
print(issubclass(io.BytesIO, io.BufferedIOBase))

# Test io.StringIO
print(isinstance(io.StringIO(), io.StringIO))
print(issubclass(io.StringIO, io.TextIOBase))

# Test io.FileIO
print(isinstance(io.FileIO(__file__), io.FileIO))
