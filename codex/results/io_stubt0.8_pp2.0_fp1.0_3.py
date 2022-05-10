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

if len(view) != 0:
    raise RuntimeError("len(view) = %d, should be 0" % len(view))
print("OK")
