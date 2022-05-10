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

# Test that the buffer was freed
gc.collect()

# The buffer should be a string now
view[0] = 'a'

# Test that the buffer was freed
gc.collect()

# The buffer should be a string now
view[0] = 'a'
