import io
# Test io.RawIOBase
f = io.BytesIO()
assert f.read() == b''
assert f.read() == b''
f.close()
assert f.read() == b''
f.close()
f = io.BytesIO(b'abc\ndef\n')
b = f.read(4)
assert b == b'abc\nd'

b = f.read(4)
assert b == b'ef\n'

b = f.read(4)
assert b == b''

b = f.read(-1)
assert b == b''

b = f.read(-1)
assert b == b''

f.seek(0)
assert f.read() == b'abc\ndef\n'
assert f.seek(10, io.SEEK_SET)
assert f.read() == b''
assert f.seek(-5, io.SEEK_END)
assert f.tell() == 5
assert f.read() == b'\ndef\n'

f.seek(0, io.SEEK_END)
assert f.tell
