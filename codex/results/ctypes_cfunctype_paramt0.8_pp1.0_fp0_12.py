import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int) 
</code>
however, when i run it, i get an error that the type of the arglist needs to be an integer. but i dont understand what it is asking for. i would appreciate if anyone can help me. 
Also, this is the error message i get when i run it:
<code>  File "./test.py", line 5, in &lt;module&gt;
    FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int) 
  File "/usr/lib64/python2.6/ctypes/__init__.py", line 749, in CFUNCTYPE
    return _CFuncPtr((restype, argtypes, flags))
  File "/usr/lib64/python2.6/ctypes/__init__.py", line 696, in _CFuncPtr
    FUNCFLAG_USE_ERRNO = 2
  File "/usr/lib64/python2.6/ctypes/__init__.py", line 339, in __init
