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

# At this point, the buffer of the io.BufferedReader object is
# holding the memory space of buf alive, even though buf is not
# referenced anymore.

print(view)
