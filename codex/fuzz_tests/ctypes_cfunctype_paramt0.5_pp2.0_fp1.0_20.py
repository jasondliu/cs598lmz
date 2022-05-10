import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

def func(x):
    return x**2

func_ptr = FUNTYPE(func)
print(func_ptr(2))
</code>
The problem is that, when I try to do something like this:
<code>import ctypes

def func(x):
    return x**2

class Foo(object):
    def __init__(self, func):
        self.func = func

f = Foo(func)

FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

f.func_ptr = FUNTYPE(f.func)

print(f.func_ptr(2))
</code>
I get the following error:
<code>TypeError: argument 1 must be a callable object
</code>
What am I doing wrong?


A:

You should use <code>ctypes.pythonapi</code> to get the address of the <code>PyCFunction_NewEx</code> function:
<code>
