import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass

def func_wrapper(func, **kw):
    return fun()

func_wrapper(lambda x: x, foo='bar')
</code>
The last line generates a <code>SystemError</code>:
<code>SystemError: Objects/functionobject.c:1082: bad argument to internal function
</code>
A similar example without the <code>FUNTYPE</code> wrapper does not generate the error, nor does the above example if I remove the keyword arguments from the <code>func_wrapper</code> invocation:
<code>def func_wrapper(func):
    return lambda x: x

func_wrapper(lambda x: x)
</code>
Any ideas what's going on here?


A:

This is a known bug with CPython 3.5 (http://bugs.python.org/issue21884). You can try to workaround it by wrapping the function you return into a regular function. Something like:
<code>def func_wrapper(func, **kw):
    def wrapper():
        return fun()
    return wrapper
</code>

