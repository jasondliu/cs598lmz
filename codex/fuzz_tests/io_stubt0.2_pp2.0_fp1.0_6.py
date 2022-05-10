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
view[0] = ord('a')

# Test that the buffer is still alive.
view[0] = ord('a')

# Test that the buffer is still alive.
view[0] = ord('a')

# Test that the buffer is still alive.
view[0] = ord('a')

# Test that the buffer is still alive.
view[0] = ord('a')

# Test that the buffer is still alive.
view[0] = ord('a')

# Test that the buffer is still alive.
view[0] = ord('a')

# Test that the buffer is still alive.
view[0] = ord('a')

# Test that the buffer is still alive.
view[0] = ord('a')

# Test that the buffer is still alive.
view[0] = ord('a')

# Test that the buffer is still alive.
view[0] = ord('a')

# Test that the buffer is still alive.
view[0] = ord('a')

#
