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

It is possible to get access to the raw underlying buffer of a Python object by using <code>PyObject_GetBuffer()</code> directly on it, but you have to make sure that no Python code can be run while accessing the buffer. In other words, you have to make sure that nothing is running synchronized with the GIL (the Python threading lock).

