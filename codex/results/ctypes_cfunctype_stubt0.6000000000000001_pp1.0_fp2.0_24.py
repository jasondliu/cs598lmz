import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
print(fun())
</code>
Output:
<code>None
</code>

However, if you are using Python 2.7, you must use <code>ctypes.c_void_p</code> instead of <code>ctypes.py_object</code> as the return type:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p)
@FUNTYPE
def fun():
    return None
print(fun())
</code>
Output:
<code>0
</code>

