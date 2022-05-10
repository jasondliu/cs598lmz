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

view[0] = ord('a')

# Test that the buffer is not deallocated after the file is closed.
# This is a regression test for http://bugs.python.org/issue15881
import gc
gc.collect()
del view
gc.collect()
