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
gc.collect()
print(view)
</code>
This prints <code>None</code> on Python 3.4.1 (CPython) on Windows, but <code>&lt;memory at 0x03D6B7A0&gt;</code> on Python 3.4.2 (PyPy 3.2.5).
I am guessing that in Python 3.4.1, the <code>io</code> module is doing something to ensure that the underlying <code>RawIOBase</code> object is properly closed.

