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
gc.collect()

# check that the internal buffer was freed
print(view)
import _testcapi
_testcapi.with_refcount(view, 1)
