import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_double)

def _make_callback(func, argname = "arg"):
    @mt.typed(None, ctypes.c_double, argname=argname)
    def _wrapper(arg: ctypes.c_double):
        func(arg.value)
    return FUNTYPE(func)
</code>
Here an example of its usage:
<code>def testfunc(val):
    print(val)

ptr_func = _make_callback(testfunc)

with open(test_file, 'r') as f:
    x = ctypes.c_double(5.5)
    ptr_func(x)
</code>

