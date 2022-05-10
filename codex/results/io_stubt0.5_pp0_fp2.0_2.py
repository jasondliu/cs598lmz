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

view[0] = ord('a')

x = io.BytesIO(view[:1])
print(x.read())

del view

print(x.read())
</code>

