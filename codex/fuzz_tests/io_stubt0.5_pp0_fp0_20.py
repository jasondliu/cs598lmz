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

# This test is only interesting with a debug build.
if not isinstance(view, memoryview):
    raise SystemExit("no memoryview")

# Check that the memoryview is still alive.
view.tobytes()

# Check that the underlying buffer is still alive.
view.tobytes()
