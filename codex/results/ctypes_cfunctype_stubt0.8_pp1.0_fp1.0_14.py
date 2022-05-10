import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

import _ctypes
_ctypes.PyObj_FromPtr(ctypes.addressof(fun))
</code>
The error message I get is
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    _ctypes.PyObj_FromPtr(ctypes.addressof(fun))
TypeError: &lt;built-in function PyObj_FromPtr&gt; returned NULL without setting an error
</code>
In contrast, when I use <code>c_void_p.in_dll(_ctypes, "PyObj_FromPtr")(ctypes.addressof(fun))</code> instead, everything works fine. I'm using the CPython master branch (i.e. Python 3.7).

