import ctypes
ctypes.cast(pointer, ctypes.py_object).value

# The following is an alternative way to do the same thing. It has the advantage that it
# does not require the ctypes module, but it does require that you know the size of the
# pointer. For example, a pointer to an int32 is 4 bytes long.
import struct
struct.unpack('i', bytearray(pointer))[0]
</code>
The following is a way to do it in Cython:
<code>from libc.stdlib cimport malloc
from cpython.ref cimport PyObject

cdef int* pointer
pointer = &lt;int*&gt; malloc(sizeof(int))
pointer[0] = 42

# The following is a way to convert the pointer to a Python int.
cdef PyObject* py_int
py_int = ((PyObject*)pointer)[0]

# The following is an alternative way to do the same thing. It has the advantage that it
# does not require the cpython.ref module, but it does require that you know the size of the
# pointer. For example,
