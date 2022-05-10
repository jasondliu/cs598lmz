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

view[0] = ord('a')

# The file object should be deallocated by now.
# If it is not, the following line will segfault.
view[0] = ord('b')
