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
print(view)

# Buffer overflow
f = io.BufferedReader(File())
f.read(2)
del f
print(view)

# Buffer underflow
f = io.BufferedReader(File())
f.read(1)
f.read(1)
del f
print(view)

# Test that the buffer is cleared when the file is closed
f = io.BufferedReader(File())
f.read(1)
f.close()
print(view)

# Test that the buffer is cleared when the file is garbage collected
f = io.BufferedReader(File())
f.read(1)
del f
print(view)
