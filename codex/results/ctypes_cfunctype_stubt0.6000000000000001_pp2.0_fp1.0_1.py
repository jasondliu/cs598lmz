import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass
fun()
</code>
Here is how to do it with ctypes.CFUNCTYPE:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(a, b):
    pass
fun(1, 2)
</code>

