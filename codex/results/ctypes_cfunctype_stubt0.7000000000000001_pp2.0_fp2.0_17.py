import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
</code>
I get the error: <code>TypeError: cannot return None in a function with restype py_object</code>.
The same happens with <code>ctypes.py_object</code> in <code>restype</code> argument of <code>ctypes.CFUNCTYPE</code>.
What is the difference between <code>ctypes.POINTER(ctypes.py_object)</code> and <code>ctypes.py_object</code>?


A:

<code>ctypes.POINTER(ctypes.py_object)</code> is a pointer to <code>ctypes.py_object</code>. 
<code>ctypes.py_object</code> is a <code>PyObject</code> (the old name for <code>PyObject*</code>) itself.
You can only return pointers to objects, not the objects itself.

