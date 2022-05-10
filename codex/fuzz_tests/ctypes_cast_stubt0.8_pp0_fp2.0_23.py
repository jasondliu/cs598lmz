import ctypes
ctypes.cast(x, ctypes.c_void_p).value
</code>
It is quite interesting to think that the actual address of <code>x</code> is a <code>PyObject*</code>, which is a pointer and thus has memory address in its own right.

