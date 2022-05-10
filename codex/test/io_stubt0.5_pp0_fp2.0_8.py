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
view

# Issue #27196: io.BufferedReader.peek() should not allocate a new buffer if
# the existing buffer is big enough.
import io

for size in [1, 2, 10, 100, 1000]:
    f = io.BytesIO(b'x' * size)
