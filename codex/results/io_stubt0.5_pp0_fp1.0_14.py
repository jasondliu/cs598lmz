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

if view[0] != 0:
    raise RuntimeError("view[0] == %d" % view[0])
