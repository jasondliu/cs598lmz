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
view
struct.unpack('@B',view)[0]

f = io.BufferedReader(File())
f.read(2)
del f
view
struct.unpack('@H',view)[0]

f = io.BufferedReader(File())
f.read(4)
del f
view
struct.unpack('@I',view)[0]

f = io.BufferedReader(File())
f.read(8)
del f
view
struct.unpack('@Q',view)[0]
