import io
# Test io.RawIOBase
print(io.RawIOBase.read)
print(io.RawIOBase.readinto)
print(io.RawIOBase.read1)
print(io.RawIOBase.readinto1)

# Test io.BufferedIOBase
print(io.BufferedIOBase.read)
print(io.BufferedIOBase.read1)
print(io.BufferedIOBase.readinto)
print(io.BufferedIOBase.readinto1)

# Test io.TextIOBase
print(io.TextIOBase.read)
print(io.TextIOBase.read1)
print(io.TextIOBase.readline)
print(io.TextIOBase.readlines)

# Test io.IOBase
print(io.IOBase.close)
print(io.IOBase.closed)
print(io.IOBase.fileno)
print(io.IOBase.flush)
print(io.IOBase.isatty)
print(io.IOBase.read)
print(io.IOBase.read1)
print(io.IOBase
