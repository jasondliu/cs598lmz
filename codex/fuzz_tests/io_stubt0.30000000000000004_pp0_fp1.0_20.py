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

# This is a bug in CPython 2.7.5.  The buffer is not cleared when the
# BufferedReader is deleted.
assert view == b'\x00'

# This is a bug in CPython 2.7.5.  The buffer is not cleared when the
# BufferedReader is closed.
f = io.BufferedReader(File())
f.read(1)
f.close()
assert view == b'\x00'

# This is a bug in CPython 2.7.5.  The buffer is not cleared when the
# BufferedReader is garbage collected.
f = io.BufferedReader(File())
f.read(1)
f = None
import gc; gc.collect()
assert view == b'\x00'
