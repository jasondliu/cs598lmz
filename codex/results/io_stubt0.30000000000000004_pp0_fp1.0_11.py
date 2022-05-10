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

# Now, the memoryview should be invalidated.
try:
    view.tobytes()
except ValueError:
    print("ValueError")
