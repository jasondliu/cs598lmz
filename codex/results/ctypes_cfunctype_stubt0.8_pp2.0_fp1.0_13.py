import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("nothing")
</code>
Calling <code>ctypes.cast(fun, ctypes.c_void_p).value</code> returns this value:
<code>140289367705240
</code>
In a C library which provides an array of function pointers, I would like to cast a list of Python functions to array of function pointers.
This is an example (which doesn't work) of how I'm doing it:
<code>import ctypes
from ctypes import c_uint
import numpy as np

def get_ptr(fun):
    return ctypes.cast(fun, ctypes.c_void_p).value

class MyClass():
    def __init__(self):
        self.myarray = np.ctypeslib.as_array((c_uint * 1)(*(get_ptr(fun),)))
        self.myarray[0] = get_ptr(fun)
        self.myfunc = (c_uint * 1).from_address(self.myarray[0])
        self.myfunc()
</code>
When I execute:
<code
