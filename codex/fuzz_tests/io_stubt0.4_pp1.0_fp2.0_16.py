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
But it looks like <code>io.BufferedReader</code> does not call <code>readinto</code> method of its raw stream.

