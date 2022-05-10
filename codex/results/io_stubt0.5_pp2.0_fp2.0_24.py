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

# a memoryview should not keep the file alive
collect()

# but it should keep the buffer alive
assert view

# and the buffer should keep the file alive
del view
collect()
