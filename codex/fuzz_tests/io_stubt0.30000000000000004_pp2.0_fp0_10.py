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
The output is <code>b'\x00'</code> on CPython 3.6.3, but <code>b''</code> on PyPy 5.10.1.

I'm not sure if this is a bug in PyPy, or if this is a bug in CPython.

