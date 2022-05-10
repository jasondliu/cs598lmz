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
The usage of <code>io</code> and <code>del</code> is to ensure that <code>self</code> is the only remaining reference to the object (preventing __del__ to be called and f to be closed).

