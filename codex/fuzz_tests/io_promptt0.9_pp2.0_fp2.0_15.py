import io
# Test io.RawIOBase
c1 = io.RawIOBase()
print(c1)

c2 = io.RawIOBase()
print(c2)

issubclass(io.FileIO, io.RawIOBase)
issubclass(io.FileIO, io.IOBase)

io.RawIOBase.readable()
io.IOBase.readable()
io.FileIO.readable()
io.TextIOBase.readable()
print(io.FileIO.readable)

io.RawIOBase.readable(c1)
io.IOBase.readable(c1)
io.FileIO.readable(c1)
io.TextIOBase.readable(c1)

# Test the io.BufferedIOBase.
b1 = io.BufferedIOBase()
print(b1)
print(b1.closed)

b2 = io.BufferedIOBase()
print(b2)
print(b2.closed)

b1.name()
print(b1.name())
b1.name = 'b1'
print(b1.name)


