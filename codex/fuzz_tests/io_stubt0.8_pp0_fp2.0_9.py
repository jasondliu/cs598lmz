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

class File(io.TextIOBase):
    def read(self, n=-1):
        global view
        return view.tobytes().decode()

f = io.TextIOWrapper(File(), encoding='latin1')
del view
f.read(1)
del f

view.tobytes()
