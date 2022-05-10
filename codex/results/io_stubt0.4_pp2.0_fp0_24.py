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

# Test that the buffer is still alive after the file is closed
view[0] = ord('x')

# Test that the buffer is still alive after the file is closed
del view

# Test that the buffer is still alive after the file is closed
view = bytearray(b'x')

# Test that the buffer is still alive after the file is closed
del view

# Test that the buffer is still alive after the file is closed
view = bytearray(b'x')

# Test that the buffer is still alive after the file is closed
del view

# Test that the buffer is still alive after the file is closed
view = bytearray(b'x')

# Test that the buffer is still alive after the file is closed
del view

# Test that the buffer is still alive after the file is closed
view = bytearray(b'x')

# Test that the buffer is still alive after the file is closed
del view

# Test that the buffer is still alive after the file is closed
view = bytearray(b'x')

# Test that
