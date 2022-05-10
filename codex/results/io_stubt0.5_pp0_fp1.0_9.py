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

# The buffer 'view' is now a memoryview of the byte array
# that was used as the buffer in the BufferedReader.
# The memoryview should not be destroyed.

# The following line should not crash.
view.tobytes()
