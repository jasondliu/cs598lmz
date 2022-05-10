import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
        view[0] = 43
    def readable(self):
        return True

f = io.BufferedReader(File(), 1)
assert f.read(1)[0] == 43
del f

# Issue #16731: A BufferedReader should be able to read its own raw buffer
# without a plain read() call.

f = io.BytesIO(b"\x82\x88\x8c")
b = io.BufferedReader(f)
assert b.readinto(bytearray(1)) == 1
assert b.peek(1) == b"\x88"
assert b.readinto(bytearray(1)) == 1
assert b.peek(1) == b"\x8c"
del b, f
