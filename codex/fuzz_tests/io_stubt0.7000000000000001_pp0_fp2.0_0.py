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
print(view)

#view = buffer(bytearray(1))
#print(view)
#print(view.tobytes())

#f.readinto(view)
