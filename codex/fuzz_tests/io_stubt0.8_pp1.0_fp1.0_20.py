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
gc.collect()
del view

view[0] = 5

gc.collect()

# check that we don't crash on an empty string
b = io.BufferedReader(io.BytesIO(b''))
b.read()
b.read()
