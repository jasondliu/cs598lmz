import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())
</code>
This works, but I don't know how to get the return value.  I can't just use the <code>return</code> statement because I don't know what the return type is.  I could use a <code>ctypes.c_char_p</code> return type, but I don't know how to convert that to a Python string.


A:

The following is a working example of how to use a ctypes callback with an unknown return type.  I'm using Python 3.7.
<code>from ctypes import *
from ctypes.wintypes import *

class StructureWithCallback(Structure):
    _fields_ = [
        ("callback", c_void_p),
    ]

def callback():
    return "hello"

callback_fun = CFUNCTYPE(c_void_p)(callback)

s = StructureWithCallback(callback_fun)

print(s.callback)
</code>

