import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
</code>
If you want to use a <code>ctypes.c_int</code> return type, you can use <code>ctypes.pythonapi</code> to get the <code>PyInt_FromLong</code> function, then call it in your function wrapper:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

# Get PyInt_FromLong from the Python API
PyInt_FromLong = ctypes.pythonapi.PyInt_FromLong
PyInt_FromLong.restype = ctypes.py_object

@FUNTYPE
def fun():
    return PyInt_FromLong(1)
</code>
This works, but unfortunately the <code>ctypes</code> API is not well defined, so you should use this with caution.

