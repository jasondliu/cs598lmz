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
After executing this I can examine the contents of <code>view</code>. This is not documented, but it is the case for CPython 2.7, 3.4 and PyPy 2.5. In fact, in PyPy <code>view</code> is a memoryview.

