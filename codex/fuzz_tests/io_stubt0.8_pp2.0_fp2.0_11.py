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

view[0] = 42
</code>
It works when I tested it on my system. I don't know how C extensions are implemented, so it might not work there.

