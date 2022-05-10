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
del view

# Test that a BufferedReader with a readinto method that returns a
# negative value is not reused.

class File(io.RawIOBase):
    def readinto(self, buf):
        return -1
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
f.read(1)
f.read(1)
del f

# Test that a BufferedReader with a readinto method that returns a
# value larger than the length of the buffer is not reused.

class File(io.RawIOBase):
    def readinto(self, buf):
        return len(buf) + 1
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
f.read(1)
f.read(1)
del f

# Test that a BufferedReader with a readinto method that returns a
# value equal to the length of the buffer is not reused.

class File(io.RawIOBase):
    def read
