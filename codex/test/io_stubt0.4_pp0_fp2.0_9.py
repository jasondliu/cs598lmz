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
del view

def f():
    global view
    view = bytearray(b"abc")
    f = io.BufferedReader(File())
    f.read(1)
    del f
    del view
    return view

