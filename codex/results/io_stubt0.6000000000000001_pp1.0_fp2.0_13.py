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
This code works in Python 2.7, but not in Python 3.5. In Python 3.5, the reference count of <code>view</code> is not updated, and <code>view</code> is deallocated after the <code>del f</code>.
I can't find any reason why this would not work in Python 3.5. Is it a bug, or am I missing something?

