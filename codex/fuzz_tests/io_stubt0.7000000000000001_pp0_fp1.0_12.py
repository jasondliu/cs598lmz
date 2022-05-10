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
view
</code>
This appears to work in Python 3.3.3 (my version), but I haven't tested this on other versions of CPython.

