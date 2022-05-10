import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
fun() # works
</code>
As an alternative, you could use <code>int</code> as the return type, instead of <code>ctypes.py_object</code>:
<code>from ctypes import CFUNCTYPE, c_int
funtype = CFUNCTYPE(c_int) # you only need to define the type once
@funtype
def fun():
    return 1
fun()
# 1
</code>
Or add an explicit <code>return</code>:
<code>@ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
    return ctypes.py_object(1)
fun() # 1
</code>

