import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "abc"
</code>
This will be more efficient than using a <code>ctypes.pythonapi</code> function, as the latter option would likely involve a Python-level function call, which is slower than a direct function call.

