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

view[0] = ord('A')

# Test that the buffer is not deallocated when the file is closed.
# This is a regression test for issue #15360.
del view
