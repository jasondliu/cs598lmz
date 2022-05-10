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

# This used to crash because the buffer was not cleared.
# Now it should not crash, but the buffer should not be cleared.
print(view)
