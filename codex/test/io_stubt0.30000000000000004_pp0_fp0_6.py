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

# Test that the buffer is not freed when the file is closed
view[0] = 0

# Test that the buffer is not freed when the file is garbage collected
del File
gc.collect()
view[0] = 0

# Test that the buffer is not freed when the file is closed and garbage collected
f = io.BufferedReader(File())
f.read(1)
del f
gc.collect()
view[0] = 0

# Test that the buffer is not freed when the file is garbage collected and closed
f = io.BufferedReader(File())
f.read(1)
del File
gc.collect()
view[0] = 0

# Test that the buffer is not freed when the file is closed and garbage collected
f = io.BufferedReader(File())
f.read(1)
del f
gc.collect()
view[0] = 0

# Test that the buffer is not freed when the file is garbage collected and closed
f = io.BufferedReader(File())
f.read(1)
del File
gc.collect()
view[0]
