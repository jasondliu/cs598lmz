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

# This is equivalent to the above, but it does not run the __del__ method
# of the BufferedReader.
view = None
File().readinto(bytearray(1))
