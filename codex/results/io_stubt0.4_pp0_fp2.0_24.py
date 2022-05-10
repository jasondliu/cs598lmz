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

print(view[0])

# Test that the file is closed when the buffer is deleted.
class File(io.RawIOBase):
    def close(self):
        global closed
        closed = True
    def readable(self):
        return True

closed = False
f = io.BufferedReader(File())
del f
print(closed)
