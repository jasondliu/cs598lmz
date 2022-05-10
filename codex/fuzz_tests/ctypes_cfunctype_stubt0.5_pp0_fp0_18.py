import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
assert fun() == 42

# Now, let's try to call it from Cython.
from cpython.ref cimport PyObject
from cpython.ref cimport Py_INCREF, Py_DECREF
from cpython.ref cimport Py_TYPE
from cpython.object cimport PyObject_Call
cdef PyObject *py_fun = &lt;PyObject *&gt;fun
cdef PyObject *result = PyObject_Call(py_fun, NULL, NULL)
print(result)
Py_DECREF(result)

# This works, but now let's try to use the Cython function
# as a callback.

cdef int callback(int a, int b):
    return a + b

cdef int call_callback(int(*callback)(int, int)):
    return callback(1, 2)

assert call_callback(callback) == 3
</code>
This works as expected. Now let's try to do the same thing with the Python function:
<code>cdef int call_callback(int(*callback)(int, int)):
    return
