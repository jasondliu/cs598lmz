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

# Test that the buffer is still alive
view[0] = 1

# Test that the buffer is still writable
view[0] = 2

# Test that the buffer is still writable
view[0] = 3

# Test that the buffer is still writable
view[0] = 4

# Test that the buffer is still writable
view[0] = 5

# Test that the buffer is still writable
view[0] = 6

# Test that the buffer is still writable
view[0] = 7

# Test that the buffer is still writable
view[0] = 8

# Test that the buffer is still writable
view[0] = 9

# Test that the buffer is still writable
view[0] = 10

# Test that the buffer is still writable
view[0] = 11

# Test that the buffer is still writable
view[0] = 12

# Test that the buffer is still writable
view[0] = 13

# Test that the buffer is still writable
view[0] = 14

# Test
