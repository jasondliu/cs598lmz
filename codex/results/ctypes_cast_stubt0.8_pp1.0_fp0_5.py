import ctypes
ctypes.cast(m, ctypes.POINTER(ctypes.c_uint32)).contents.value
</code>
But that seems to be an abuse. 
I am specifically looking for C/Python_C-API way to do this. Not a ctypes conversion.


A:

Here is one way to solve it:
<code>import ctypes

class PyArrayObject_Fields(ctypes.Structure):
    _fields_ = [
        ('ob_refcnt', ctypes.c_ssize_t),
        ('ob_type',   ctypes.py_object),
        ('ob_size',   ctypes.c_ssize_t),
        ('nd',        ctypes.c_int),
        ('dimensions',ctypes.py_object),
        ('data',      ctypes.py_object),
        ('descr',     ctypes.py_object),
        ('flags',     ctypes.c_int)]

# Now, get the fields and convert them to an int
pyint = np.int32(1)
pyint_ptr = ctypes.py
