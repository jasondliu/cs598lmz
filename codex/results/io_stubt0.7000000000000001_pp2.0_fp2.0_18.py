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

view = None

# This did not crash:
io.FileIO.readinto(io.FileIO(), bytearray())

# This did crash:
f = io.FileIO()
f.readinto(bytearray())
f.close()
