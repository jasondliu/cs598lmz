import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"
fun()
</code>
If you want to return a string from C and use it from Python, you need to use <code>Py_BuildValue</code>.

