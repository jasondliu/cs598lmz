import ctypes
ctypes.cast(ctypes.addressof(self.item), ctypes.POINTER(ctypes.c_int))
</code>
However, if you are in Cython and don't have to deal with Cython's type system, you can cast directly from <code>int</code> to <code>POINTER(c_int)</code> using the <code>cdef</code> keyword.
<code>from cpython cimport array as c_array
cdef c_int *p = &lt;c_int*&gt;self.item
</code>
The result is the same (a pointer to the first element of <code>self.item</code>), but the second version is more efficient.

