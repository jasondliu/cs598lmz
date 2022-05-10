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

# Verify that the file object has been deallocated
import gc
gc.collect()
if gc.collect() != 0:
    print "error: File object not deallocated"

# Issue #6306: io.TextIOWrapper left an internal buffer allocated
import io
f = io.TextIOWrapper(io.BytesIO())
f.close()
del f
gc.collect()
if gc.collect() != 0:
    print "error: io.TextIOWrapper internal buffer not deallocated"
