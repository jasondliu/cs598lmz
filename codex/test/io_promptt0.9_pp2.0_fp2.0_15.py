import io
# Test io.RawIOBase
c1 = io.RawIOBase()
print(c1)

c2 = io.RawIOBase()
print(c2)

issubclass(io.FileIO, io.RawIOBase)
issubclass(io.FileIO, io.IOBase)

