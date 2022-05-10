import io
# Test io.RawIOBase class existence
hasattr(io, 'RawIOBase')

# Check similar classes too
hasattr(io, 'BufferedIOBase')
hasattr(io, 'TextIOBase')

# RawIOBase - subclass of IOBase
issubclass(io.RawIOBase, io.IOBase)

# Creating file stream for raw bytes
rw = io.BytesIO(b'abc')
type(rw)

# With the help of the constructor, we get an object that works
# like a file stream.
rw.read()
rw.write(b'def')
rw.read()

# Test seek and tell
rw.seek(1)
rw.read()
rw.tell()

# Test opening file via io module
rw = io.open('test.dat', 'wb')
type(rw)

# Write
rw.write(b'a')
rw.write(b'b')
rw.write(b'c')
rw.close()

# Read via simple
f = open('test.dat', 'rb')
f.read()
f.close()

