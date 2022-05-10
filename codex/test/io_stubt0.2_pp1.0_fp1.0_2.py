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

# Test that the file is closed when the buffer is deleted
class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True
    def close(self):
        global closed
        closed = True

closed = False
f = io.BufferedReader(File())
del f
closed

# Test that the file is closed when the buffer is deleted, even if
# the buffer is not fully read
class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True
    def close(self):
        global closed
        closed = True

closed = False
f = io.BufferedReader(File())
f.read(1)
del f
closed

# Test that the file is closed when the buffer is deleted, even if
# the buffer is not fully read and the file is closed
