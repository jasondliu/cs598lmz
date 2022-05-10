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

# Test that the buffer is not freed.
print(view[0])

# Test that the buffer is freed when the file is closed.
f = io.BufferedReader(File())
f.read(1)
f.close()
del f

# Test that the buffer is not freed when the file is closed, but the
# buffer is freed when the buffer is closed.
f = io.BufferedReader(File())
b = f.read(1)
f.close()
del f
del b

# Test that the buffer is not freed when the file is closed, but the
# buffer is freed when the buffer is closed.
f = io.BufferedReader(File())
b = f.read(1)
del f
del b

# Test that the buffer is not freed when the file is closed, but the
# buffer is freed when the buffer is closed.
f = io.BufferedReader(File())
b = f.read(1)
del b
f.close()
del f

# Test that the buffer is freed when the file is closed, but the
# buffer is
