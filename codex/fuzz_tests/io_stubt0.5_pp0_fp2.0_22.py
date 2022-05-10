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

# This test is a bit more complicated than it needs to be, because
# it's not possible to create a file-like object with a readinto()
# method that doesn't also have a read() method.

print(view)
