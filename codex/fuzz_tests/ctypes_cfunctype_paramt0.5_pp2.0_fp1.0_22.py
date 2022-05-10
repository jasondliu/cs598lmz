import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def wrap(function):
    return FUNTYPE(function)

def test_function(x):
    return x**2

wrapped_test_function = wrap(test_function)

print wrapped_test_function(3.0)
</code>
The output is:
<code>9.0
</code>

