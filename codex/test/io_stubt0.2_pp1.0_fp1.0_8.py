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

# Test that the buffer is not freed when the BufferedReader is deleted
# (the buffer is still referenced by the view).
view[0] = 0

# Test that the buffer is freed when the view is deleted.
del view

# Test that the buffer is freed when the BufferedReader is deleted
# (the buffer is still referenced by the view).
view = bytearray(b"abc")
f = io.BufferedReader(File())
f.read(1)
del f
view[0] = 0

# Test that the buffer is freed when the view is deleted.
del view

# Test that the buffer is freed when the BufferedReader is deleted
# (the buffer is still referenced by the view).
view = memoryview(b"abc")
f = io.BufferedReader(File())
f.read(1)
del f
view[0] = 0

# Test that the buffer is freed when the view is deleted.
del view

# Test that the buffer is freed when the BufferedReader is deleted
# (the buffer is still referenced by the view).
