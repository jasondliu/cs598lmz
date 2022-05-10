import io
# Test io.RawIOBase methods
print('RawIOBase    ', hasattr(io.RawIOBase, 'seekable'))
print('RawIO        ', hasattr(io.RawIO, 'seekable'))
print('FileIO       ', hasattr(io.FileIO, 'seekable'))
print('BufferedIOBase', hasattr(io.BufferedIOBase, 'seekable'))
print('BufferedIO   ', hasattr(io.BufferedIO, 'seekable'))
print('BytesIO      ', hasattr(io.BytesIO, 'seekable'))
print('StringIO     ', hasattr(io.StringIO, 'seekable'))
print('TextIOBase   ', hasattr(io.TextIOBase, 'seekable'))
print('TextIOWrapper', hasattr(io.TextIOWrapper, 'seekable'))
print('BufferedWriter', hasattr(io.BufferedWriter, 'seekable'))
print('BufferedReader', hasattr(io.BufferedReader, 'seekable'))
print('BufferedRWPair', hasattr(io.BufferedRWP
