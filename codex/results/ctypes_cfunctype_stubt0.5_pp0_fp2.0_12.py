import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello, world!"

def fun_wrapper(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        return fun(*args, **kwargs)
    return wrapper
</code>
I can't seem to get the <code>@wraps</code> decorator to work in this case.  I've tried using <code>@fun_wrapper</code> and <code>@fun_wrapper(fun)</code> but neither of these work.  Is there a way to get this to work?


A:

The <code>@wraps</code> decorator is used to decorate the wrapper function, not the wrapped function.  So you need to decorate the <code>wrapper</code> function in <code>fun_wrapper</code>:
<code>def fun_wrapper(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        return fun(*args, **kwargs)
    return wrapper
</code>

