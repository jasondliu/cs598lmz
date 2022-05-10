import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print fun()
</code>
It works and returns 42.
However, when I try to compile it using Cython, it gives me the error:
<code>$ cython test.pyx

Error compiling Cython file:
------------------------------------------------------------
...
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
^
------------------------------------------------------------

test.pyx:5:14: 'ctypes.py_object' is not a type identifier
</code>
Why is Cython giving me this error? Is there a way to fix it?


A:

This is a bug in cython, which has now been fixed.
https://github.com/cython/cython/issues/1698

