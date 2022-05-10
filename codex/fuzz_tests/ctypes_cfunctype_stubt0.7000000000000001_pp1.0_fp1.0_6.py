import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return

import _ctypes
_ctypes.PyObj_FromPtr(ctypes.cast(fun, ctypes.c_void_p).value)
</code>
Fails with:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ArgumentError: argument 1: &lt;class 'TypeError'&gt;: expected LP_PyObject instance instead of _FuncPtr instance
</code>
So, as you can see, <code>PyObj_FromPtr</code> does not accept <code>_FuncPtr</code> instances.

