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

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = memoryview(buf)
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
print(view)

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = memoryview(bytearray(buf))
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
print(view)

# Issue #19056
# This used to crash because of a Py_DECREF() after decrefing the
# buffer object to zero.
io.BytesIO().readinto(bytearray(1))
