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

class Output:
    buf = None
    def write(self, data):
        global view
        view = data

o = Output()
