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
It uses a <code>RawIOBase</code>-compatible object to provide the buffer, and the <code>BufferedReader</code> does the actual buffering.  There's a lot of copying happening, but it all seems to work.

