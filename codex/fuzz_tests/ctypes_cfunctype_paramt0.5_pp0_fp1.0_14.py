import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

class MyFunc(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, x):
        return self.func(x)
</code>
Now I can do:
<code>&gt;&gt;&gt; func = MyFunc(lambda x: x*x)
&gt;&gt;&gt; ctypes_func = FUNTYPE(func)
&gt;&gt;&gt; ctypes_func(1.2)
1.4400000000000002
</code>

