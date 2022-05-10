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
Cython:
<code>from libc.stdio cimport FILE
cimport cython
cdef class File:
    cdef char *view
    def __cinit__(self):
        self.view = &lt;char *&gt;malloc(1)
    cython.declare(f=FILE)
    def readable(self):
        return True
    def __dealloc__(self):
        free(self.view)
</code>
Cython:
<code>from libc.stdio cimport FILE
from cpython.buffer cimport Py_buffer
from cython.view cimport array as cvarray
cimport cython

cdef class File:
    cdef char *view
    def __cinit__(self):
        self.view = &lt;char *&gt;malloc(1)
    cython.declare(f=FILE)
    def readable(self):
        return True
    def __dealloc__(self):
        free(self.view)

    def readinto(self
