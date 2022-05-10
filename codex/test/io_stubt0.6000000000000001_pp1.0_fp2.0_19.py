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

# test that the file object is closed
f = io.BufferedReader(File())
f.close()
try:
    f.read(1)
except ValueError:
    pass
else:
    raise RuntimeError("expected a ValueError")

# test that the buffer is cleared when the file object is closed
f = io.BufferedReader(File())
f.read(1)
f.close()
try:
    f.read(1)
except ValueError:
    pass
else:
    raise RuntimeError("expected a ValueError")

# verify that the weakref callback is called
import weakref
def callback(x):
    global called
    called = 1
f = io.BufferedReader(File())
ref = weakref.ref(f, callback)
del f
called = 0
del ref
