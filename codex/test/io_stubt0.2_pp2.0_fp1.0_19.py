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
view[0] = ord('x')

# Check that the buffer is still writable
view[0] = ord('y')

# Check that the buffer is still writable
view[0] = ord('z')

# Check that the buffer is still writable
view[0] = ord('a')

# Check that the buffer is still writable
view[0] = ord('b')

# Check that the buffer is still writable
view[0] = ord('c')

# Check that the buffer is still writable
view[0] = ord('d')

# Check that the buffer is still writable
view[0] = ord('e')

# Check that the buffer is still writable
view[0] = ord('f')

# Check that the buffer is still writable
view[0] = ord('g')

# Check that the buffer is still writable
view[0] = ord('h')

# Check that the buffer is still writable
view[0] = ord('i')

# Check
