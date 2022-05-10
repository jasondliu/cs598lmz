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
buf = view
del view
buf[0] = 1 # Crash.
</code>
This problem seems to be fixed in Python 3.

