import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double,ctypes.c_double)

def make_func(f):
    return FUNTYPE(f)

def get_func(f):
    return f

def make_func_array(f):
    return FUNTYPE * len(f)

def get_func_array(f):
    return f

def make_func_ptr(f):
    return ctypes.cast(f, FUNTYPE)

def get_func_ptr(f):
    return ctypes.cast(f, ctypes.POINTER(FUNTYPE))
</code>
And a test:
<code>&gt;&gt;&gt; f = make_func(lambda x: x**2)
&gt;&gt;&gt; f(2.0)
4.0
&gt;&gt;&gt; f = get_func(f)
&gt;&gt;&gt; f(2.0)
4.0
&gt;&gt;&gt; f = make_func_array([lambda x: x**2, lambda x:
