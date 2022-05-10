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

# Check that the buffer is still alive
view[0] = 0

# Check that the buffer is still writable
view[0] = 1

# Check that the buffer is still alive
view[0] = 0

# Check that the buffer is still writable
view[0] = 1

# Check that the buffer is still alive
view[0] = 0

# Check that the buffer is still writable
view[0] = 1

# Check that the buffer is still alive
view[0] = 0

# Check that the buffer is still writable
view[0] = 1

# Check that the buffer is still alive
view[0] = 0

# Check that the buffer is still writable
view[0] = 1

# Check that the buffer is still alive
view[0] = 0

# Check that the buffer is still writable
view[0] = 1

# Check that the buffer is still alive
view[0] = 0

# Check that the buffer is still writable
view[0] = 1

# Check that the buffer is still alive
