import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "test"
fun()

# ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
# &lt;class 'ctypes.CFUNCTYPE'&gt;
# ctypes.CFUNCTYPE(ctypes.py_object)
# &lt;class 'ctypes.CFUNCTYPE'&gt;
# ctypes.CFUNCTYPE(ctypes.py_object)(lambda: "test")
# &lt;ctypes.CFUNCTYPE object at 0x7f7c5e0bea10&gt;
# ctypes.CFUNCTYPE(ctypes.py_object)(lambda: "test")()
# &lt;ctypes.CFUNCTYPE object at 0x7f7c5e0bea10&gt;
# ctypes.CFUNCTYPE(ctypes.py_object)(lambda: "test")()()
# 'test'
