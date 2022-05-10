import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return b'abc'

ctypes.pythonapi.PyObject_SetAttr.argtypes = (ctypes.py_object, ctypes.py_object, ctypes.py_object)

ctypes.pythonapi.PyObject_SetAttr(
    ctypes.py_object(TypeError),
    ctypes.py_object(b'__str__'),
    ctypes.py_object(fun)
)

x = TypeError()
print(x)
</code>
Output:
<code>abc
</code>

