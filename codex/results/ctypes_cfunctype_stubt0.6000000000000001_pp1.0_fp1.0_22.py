import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(fun())
</code>
This code works fine but, as you can see, I'm using the <code>ctypes</code> library, which is not a standard library. Is there any way to achieve the same result without using <code>ctypes</code>?


A:

I'm not sure if this is the "best" or "most correct" way to do it. But it works.
<code>import ctypes

def make_callable(func):
    return ctypes.CFUNCTYPE(ctypes.py_object)(func)

@make_callable
def fun():
    return 42

print(fun())
</code>

