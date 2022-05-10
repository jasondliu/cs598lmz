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

with io.BufferedReader(File()) as f:
    f.read(1)

with io.BytesIO(view) as f:
    assert f.read(1) == 'h'
