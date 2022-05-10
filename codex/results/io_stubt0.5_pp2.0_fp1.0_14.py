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
del File
</code>
This works because the <code>io.BufferedReader</code> object will call <code>readinto</code> on the <code>File</code> object, which will set the <code>buf</code> variable (which is a reference to a <code>bytearray</code> object) to the <code>view</code> variable, which is a global variable.

