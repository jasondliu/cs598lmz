import io
class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True
f = io.BufferedReader(File())
f.read(1)
def f():
    view[0] = 42
f()
