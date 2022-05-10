import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None
</code>
In the above code, the <code>None</code> is not a valid return type, but it is not detected by the compiler. 
I tried to use <code>ctypes.c_void_p</code> instead of <code>ctypes.py_object</code>, but the compiler still cannot detect the invalid return type.
Is there any way to detect the invalid return type?


A:

The code you have is valid. The <code>ctypes.py_object</code> type is a Python object. <code>None</code> is a Python object. So, returning <code>None</code> is a valid operation.

