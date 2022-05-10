import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_void_p)
def func(a, b):
    print(a, b)
    return a + b

CALLBACK = FUNTYPE(func)

lib.call_callback(CALLBACK)
</code>
output:
<code>1 &lt;__main__.LP_c_void_p object at 0x7f8f7d6d1e40&gt;
</code>
I don't know why the second parameter is an object instead of a number.

