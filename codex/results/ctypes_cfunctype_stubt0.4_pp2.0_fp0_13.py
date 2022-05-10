import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

fun()
</code>
This works, but it's not very fast. 
I also tried to use <code>ctypes.CFUNCTYPE(ctypes.c_char_p)</code> as the function type, but I can't get that to work.
Is there a way to use <code>ctypes</code> to return a <code>char*</code>?


A:

You can use <code>ctypes.c_char_p</code> as the return type if you return a <code>bytes</code> object.  <code>bytes</code> is a <code>char*</code> in C.
<code>from ctypes import *

FUNTYPE = CFUNCTYPE(c_char_p)

@FUNTYPE
def fun():
    return b'hello'

print(fun())
</code>

