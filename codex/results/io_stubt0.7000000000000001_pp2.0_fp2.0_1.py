import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f # This should trigger a flush
f = io.StringIO()
ctypes.memmove(f.write_buf, view, 1)
f.seek(0)
s = f.read()
assert repr(s) == "'t'"

# Test a BufferedRWPair
import io
import _io

class TestRW:
    def __init__(self, data):
        self.data = io.BytesIO(data)
    def read(self, n):
        return self.data.read(n)
    def write(self, b):
        self.data.seek(0)
        self.data.write(b)
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return True

r = TestRW(b'abcde')
w = TestRW(b'xyzzy')
b = _io.BufferedRWPair(r, w)
assert b.read(1) == b'a'
assert b.read(1) == b'b'
assert b.
