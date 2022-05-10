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

# The write barrier should not call finalizers for the above File()
# instance, since it was already tracked by the GC.

view[0] = 1
for i in range(12):
    del view
    if i % 2 == 0:
        f = io.BytesIO()
    else:
        f = io.StringIO()
    del f

del view
collect()

# Make sure that the File() instance is gone, and that calling its
# finalizer didn't mess up the GC.  This should not crash.
f = io.BufferedReader(File())
del f
collect()

# Same test with bytearray

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

view[0] = 1
for i in range(12):
    del view
    if i % 2 == 0:
        f = io.BytesIO()
   
