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
del File

# Since the file is closed, the memory pointed at by buf is invalid.
# However, the memoryview object is still alive, and its buf
# attribute holds a reference to the invalid memory.

mv = memoryview(view)
mv.tolist()

# Exit with a crash.
