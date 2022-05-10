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
view[0] = ord('A')

class File(io.RawIOBase):
    def readinto(self, buf):
        pass
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read()
f.read()
f.read()
del f

# Issue #17280: check that the internal _read_buf is not
# released prematurely by the GC
f = io.BytesIO()
f._read_buf = bytearray(3)
del f

# Issue #17280: check that the internal _write_buf is not
# released prematurely by the GC
f = io.BytesIO()
f._write_buf = bytearray(3)
del f

b = io.BufferedReader(io.BufferedReader(io.BytesIO(b"a b c")))
print(list(b), list(b), list(b), list(b), list(b))

f = io.BytesIO(b"abc")
b = io.BufferedReader(f, 3)
b.
