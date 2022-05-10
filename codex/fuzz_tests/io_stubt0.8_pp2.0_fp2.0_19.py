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
print(view)
assert len(view) == 1

f = io.BufferedRandom(File())
f.read(1)
del f
print(view)
assert len(view) == 1

f = io.BufferedRWPair(File(), File())
f.read(1)
del f
print(view)
assert len(view) == 1

f = io.BufferedWriter(io.BufferedReader(File()))
f.write(b'x')
del f
print(view)
assert len(view) == 1

f = io.BytesIO()
f.write(b'x')
del f

f = io.BytesIO()
f.writelines((b'x', b'x'))
del f

f = io.BytesIO()
f.writelines((b'x', b'x'), 'y')
del f

f = io.BytesIO()
b = bytearray(b'x')
f.write(b)
f.seek(0)
print(f.read())
del f


