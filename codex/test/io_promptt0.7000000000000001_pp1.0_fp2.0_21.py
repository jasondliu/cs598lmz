import io
# Test io.RawIOBase
fh = io.BytesIO('abc\ndef\n'.encode())
fh.readline() == b'abc\n'

fh = io.BytesIO(b'abc\n')
fh.readline() == b'abc\n'
 
fh = io.BytesIO(b'abc\nd')
fh.readline() == b'abc\n'

fh = io.BytesIO(b'abc\ndef\n')
fh.readline(4) == b'abc\n'

fh = io.BytesIO(b'')
fh.readline() == b''

fh = io.BytesIO(b'abc\ndef\n')
fh.readline() == b'abc\n'
fh.readline() == b'def\n'
fh.readline() == b''

fh = io.BytesIO(b'abc\ndef\n')
fh.readlines() == [b'abc\n', b'def\n']

fh = io
