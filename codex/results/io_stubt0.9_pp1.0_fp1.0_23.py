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

view[:] = b'x'
</code>
In CPython 3.2.2, it crashes when deleting <code>f</code>, in PyPy 2.1 it is fine. Are they non-conforming implementations?
Filed as PyPy issue 668.
EDIT: Updated the title (originally "CPython 3.2 leaking memory when using buffered I/O", but that turned out to be unrelated).


A:

You're calling <code>PEP 3118</code> functions with the wrong <code>Py_buffer</code>, hence your "crash".
In addition, you'd need to release the buffer that <code>py_buffer</code> points to, since a <code>Py_buffer</code> struct is not a <code>Py_buffer</code> struct, but a pointer to a <code>Py_buffer</code> struct.

