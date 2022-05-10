import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"
</code>
I get the following error:
<code>TypeError: in method 'PyCFuncPtr_New', argument 2 of type 'PyObject *'
</code>
I've tried to change the <code>FUNTYPE</code> to be <code>ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)</code> but this doesn't seem to work either.
Any idea on how to solve this?

