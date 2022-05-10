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

print(view)
</code>
It's not a very good example, but it demonstrates that the buffer returned by <code>readinto()</code> can live longer than the <code>BufferedReader</code> object.

