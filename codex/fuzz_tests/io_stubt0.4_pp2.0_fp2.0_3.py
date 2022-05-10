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

# This will crash
view[0] = 1
</code>
The crash occurs because <code>io.BufferedReader</code> does not call <code>Py_DECREF</code> on the raw file object when the buffered reader is deleted.

