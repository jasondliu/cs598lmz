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


class File2(io.RawIOBase):
    def readable(self):
        return True

f = io.BufferedReader(File2())
try:
    f.read(1)
except io.UnsupportedOperation:
    pass
else:
    raise Exception("io.UnsupportedOperation not raised")
del f


class File3(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def fileno(self):
        return 42
    def readable(self):
        return True

f = io.BufferedReader(File3())
assert(f.fileno() == 42)

f = io.BufferedReader(io.BytesIO(b"abc"))
assert f.read(1) == b"a"
assert f.read(1) == b"b"
assert f.read(1) == b"c"

s = io.BytesIO(b"abc")
r = io.BufferedReader(s)
r.seek(1)
assert r.read(1) == b'
