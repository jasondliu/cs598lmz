import ctypes
# Test ctypes.CFUNCTYPE

libc = ctypes.CDLL(ctypes.util.find_library("c"))

# create a function-pointer-type
PyObject_FromVoidPtr = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.c_void_p)
# create a function-pointer-object
PyObject_FromVoidPtrFunc = PyObject_FromVoidPtr(
    # the address of the C function to call
    libc._PyObject_FromVoidPtr,
    # True means that the function returns a new reference
    True)

# Now we can call the function pointer just like any other Python callable
o = PyObject_FromVoidPtrFunc(id(PyObject_FromVoidPtrFunc))
print o
print o is PyObject_FromVoidPtrFunc
</code>
Output:
<code>&lt;CFUNCTYPE object at 0x7f0fbc5d5a00&gt;
False
</code>
Note that the function pointer object is not the same as the function pointer type (as in C).
