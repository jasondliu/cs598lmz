import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

class Callable(object):
    def __init__(self, callable):
        self._callable = callable

    def __call__(self, *args):
        return self._callable(*args)

def callback(callable):
    """
    Decorator that converts a function into a callback function.  This
    is necessary because some functions require a callback function
    pointer as an argument.  In Python, these are usually implemented
    as methods, which are not the same as function pointers.  So,
    this decorator will convert the function into a global function
    pointer that can be passed to C code.
    """
    name = callable.__name__
    func_type = FUNTYPE(callable.func_code.co_argcount)
    func = func_type(callable)
    globals()[name] = func
    return Callable(func)
</code>
Now, you can decorate a function like this:
<code>@callback
def foo(x):
    return x
</code>
And it will
