import io
# Test io.RawIOBase(file object)
f = StringIO()
f.write('test')
f.seek(0)
f.tell()
f.read(4) # read only the first four bytes

# for more io example, see io.IOBase

# Test io.StringIO(str)
f = io.StringIO()
f.write('string')
print(f.getvalue())
# it has all the write functions from io.IOBase


# Test io.BytesIO(bytes)
# it has all the write functions from io.IOBase and io.BufferedIOBase
# it is a buffered stream for bytes only
f = io.BytesIO()
f.write(b'bytes')
print(f.getvalue())
f.seek(0)
f.read(5) # read first 5 bytes
