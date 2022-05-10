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

# test that the buffer was released
import gc
gc.collect()

# test that the buffer was really released
import _testcapi
