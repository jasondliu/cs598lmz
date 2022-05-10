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
del view

# Issue #24071: test that the destructor of a BufferedReader doesn't try to
# access the underlying file object after it has been closed.
class File(io.RawIOBase):
    def readinto(self, buf):
        pass
    def close(self):
        raise ValueError("shouldn't be called")

