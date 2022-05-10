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

# Test that the buffer is still alive.
print(view)

# Test that the file is closed.
try:
    f.read(1)
except ValueError:
    pass
else:
    print("f.read(1) didn't raise ValueError")

# Test that the buffer is still alive.
print(view)
