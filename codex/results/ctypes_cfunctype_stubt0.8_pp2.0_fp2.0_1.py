import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass

print(fun.__name__)
</code>


A:

Your original code has a serious bug; you're trying to use <code>ctypes.py_object</code> as a return type and an argument type, but <code>ctypes.py_object</code> is only valid as a return type.  (It's a "restrictive type," in ctypes terminology.)  The error message is about the argument type:
<code>Traceback (most recent call last):
  File "prog.py", line 3, in &lt;module&gt;
    @FUNTYPE
TypeError: must be a C function type or function
</code>
When you change the return type from <code>ctypes.py_object</code> to <code>ctypes.c_int</code>, the error message goes away, because the @decorator syntax doesn't cause the validation of the argument types until the decorated function is called, which it isn't in the new example.

