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
print(sys.getrefcount(view))

# This is a test of the reference count of the buffer returned by
# BufferedReader.read().  It should be 1.
#
# On 32-bit platforms, the buffer is allocated by PyString_FromStringAndSize
# which calls PyMem_Malloc.  PyMem_Malloc returns a pointer to uninitialized
# memory, so the reference count is 1.
#
# On 64-bit platforms, the buffer is allocated by _PyObject_NewVar.  This
# function calls PyObject_InitVar which sets the reference count to 1.
#
# On all platforms, the reference count is decremented by Py_DECREF in
# PyBuffer_Release.  This function is called by the tp_dealloc function of
# PyStringObject (in stringobject.c).  The reference count is incremented
# by Py_INCREF in PyBuffer_Release.  This function is called by
# PyObject_GetBuffer and PyObject_GetWriteBuffer (in getbuffer.c).
#
# If the reference count is not 1,
