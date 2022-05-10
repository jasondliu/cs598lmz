import io
# Test io.RawIOBase
print('Test io.RawIOBase:')

raw_file = io.RawIOBase()
print('tmp file is at', raw_file.fileno())

# Test io.BufferedRawIOBase

print('Test io.BufferedRawIOBase:')

buffered_file = io.BufferedRawIOBase()
print('tmp file is at', buffered_file.fileno())

# Test io.ByteIOBytes and io.BytesIO

print('Test io.ByteIOBytes and io.BytesIO:')

byte_file = io.BytesIO()
print('tmp file is at', byte_file.fileno())

# Test io.IOBase

print('Test io.IOBase:')

io_file = io.IOBase()
print('tmp file is at', io_file.fileno())

# Test io.RawIOBase
print('Test io.FileIO:')

file_file = io.FileIO()
print('tmp file is at', file_file.fileno())


# Test io.BufferedIOBase

print('
