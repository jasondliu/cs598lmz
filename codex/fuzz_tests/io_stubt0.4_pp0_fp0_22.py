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
</code>
The <code>view</code> is not a copy of the <code>buf</code> object, but a view of the same object.

