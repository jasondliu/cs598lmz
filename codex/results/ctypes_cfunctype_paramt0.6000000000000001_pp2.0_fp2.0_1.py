import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
def make_c_function(python_function):
    return FUNTYPE(python_function)
</code>
Then, you can use the <code>ctypes</code> module to call the function in Python:
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; lib = ctypes.CDLL('libc_shared.so')
&gt;&gt;&gt; result = lib.c_function(make_c_function(lambda x: x**2))
&gt;&gt;&gt; result
1.0
</code>

