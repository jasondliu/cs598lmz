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
This prints <code>b''</code> on Python 3.6, and <code>b'\x00\x00\x00\x00\x00\x00\x00\x00'</code> on Python 3.7.
The difference is that <code>_pyio.TextIOWrapper</code> buffer allocation uses <code>PyMem_Malloc</code> on Python 3.6 and <code>PyMem_RawMalloc</code> on Python 3.7.
It is not clear to me which one of these behaviours is a bug.

