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

# io.BytesIO
f = io.BytesIO()
f.write(b'abc')
print(f.getvalue())

# io.StringIO
f = io.StringIO()
f.write('abc')
print(f.getvalue())

# io.TextIOWrapper
f = io.TextIOWrapper(io.BytesIO(), encoding='utf-8')
f.write('abc')
