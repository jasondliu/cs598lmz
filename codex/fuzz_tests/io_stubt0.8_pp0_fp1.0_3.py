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

# This should not crash
bytes(buf)
del buf

# Issue #20983: don't crash on a file opened directly with os.open().
import os
fd = os.open(__file__, os.O_RDONLY)
f = io.BufferedReader(os.fdopen(fd, "r"))
f.read(1)
del f
del File
