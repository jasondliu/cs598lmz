import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
ctypes.pythonapi.PyObject_CallFunction(fun, None)
</code>
But it crashes with this error:
<code>Fatal Python error: Segmentation fault
</code>
How can I call a function with no arguments?
(I need this to call a function in a C extension module, which happens to have no arguments.)


A:

You need to pass a <code>NULL</code> pointer.
<code>ctypes.pythonapi.PyObject_CallFunction(fun, ctypes.c_void_p())
</code>

