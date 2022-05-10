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

class File(io.RawIOBase):
    def write(self, buf):
        pass
    def writable(self):
        return True

f = io.BufferedWriter(File())
f.write(view)
del f

# Check that the original buffer has not been modified
print(sum(view))
