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
Output:
<code>bytearray(b'')
</code>
(I don't know how to read the buffer, but it's empty, so it's probably not a problem of the buffer getting overwritten. In the real code, I don't have <code>global</code>.)


A:

Short answer: Cython will not call any Python code during initialization of the buffer in <code>view[:]</code>; for that, you'll have to use the iteration syntax <code>view[i]</code>.
Long answer:
As explained by DavidW in the comments, CPython does not optimize and execute <code>view[:]</code> into an array initializer, thus making it impossible for Cython to know to translate it as an array initializer in C.
However, Cython can be instructed to use a C loop by using the variable the variable <code>i</code> inside the slice.
<code>from io import RawIOBase
import cython
cimport cython

cdef class File(RawIOBase):
    def readinto(self
