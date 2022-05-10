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

# https://docs.python.org/3/library/io.html#io.BufferedReader.readinto
# https://docs.python.org/3/library/io.html#io.RawIOBase.readinto
# https://docs.python.org/3/library/io.html#io.RawIOBase.readable
# https://docs.python.org/3/library/io.html#io.BufferedReader.read
