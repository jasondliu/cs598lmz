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
print(view)

# Test that the buffer is released, at least on PyPy
import gc
gc.collect()

# Test that the buffer is released, at least on CPython
import ctypes
