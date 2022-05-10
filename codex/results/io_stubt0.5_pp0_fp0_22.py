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
The <code>del f</code> at the end is important: it's the only way to make <code>f</code> release the <code>view</code> it's holding.

