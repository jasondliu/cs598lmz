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

view[0] = 0

# This should not crash.
import _io
_io.FileIO.readinto(File(), view)

# This should not crash.
import _io
_io.FileIO.readinto(File(), view)
