import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return CPyMarshal.read_python_long(0)

v = cast(funPtr.value, FUNTYPE)
</code>
You can change the place where I supplied raw <code>0</code> with the marshalled value, that is returned by <code>PYTHON_API_MANAGED_CALL_FUNC</code>, and probably something like this should work.

