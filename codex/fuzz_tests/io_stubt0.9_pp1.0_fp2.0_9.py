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
After a <code>readinto</code> call, the buffer's lifetime is tied to that of the <code>BufferedReader</code> object.
This means that in CPython, the buffer isn't freed automatically, but in PyPy it is. If a <code>readinto</code> call is followed by another <code>read</code> call (as in the <code>f.read(1)</code> above), the buffer must be preserved.

