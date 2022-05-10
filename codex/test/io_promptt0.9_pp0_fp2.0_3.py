import io
# Test io.RawIOBase
# try raw_input in python 2, fallback to input in python 3
try:
    input = raw_input
except NameError:
    pass

buf = io.BytesIO()
print('{!r}'.format(buf))
buf.write('abc'.encode())
#   returns the number of bytes written
print('{!r}'.format(buf.getvalue()))
buf.seek(1)
print('{!r}'.format(buf.read(1)))
buf.seek(0)
print('{!r}'.format(buf.read(2)))
buf = io.BytesIO(b'initial value')
print('{!r}'.format(buf.read()))
# Underlying buffer can be exposed as a byte array
buf = io.BytesIO()
print('{!r}'.format(buf))
buf.write(b'abc')
buf.seek(0)
print('{!r}'.format(buf.read()))
# File I/O that closely maps to the built-in file is also available
