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

# This is the place where the actual bug hit:
# A GC was triggered while the PyObject was still
# pointing to the ctypes object.
del view

# This is necessary to trigger a GC in the testsuite
import gc; gc.collect()
