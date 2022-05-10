import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(fun())
</code>
If you want your C function to take arguments, make a python function (which will be marshalled to C) then make a python function that calls that C function. Pass that second function to the C api that takes a python function.
<code>from ctypes import *

def pyndo_c_function(py_function):
    api = get_api()
    f = FUNCTYPE(c_int)(py_function)
    ret = api.register(0, c_void_p.from_buffer(f))
    if ret == -1:
        return False
    return True

def python_function(x):
    return x*2
</code>

