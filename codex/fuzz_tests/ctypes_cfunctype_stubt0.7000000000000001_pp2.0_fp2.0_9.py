import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
   return [[1]]

def g(x):
    return x

g(fun())
</code>
The code above can be run without error.
However, the following code:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

def foo():
    @FUNTYPE
    def fun():
       return [[1]]
    return fun

def g(x):
    return x

g(foo())
</code>
will raise error: TypeError: int() argument must be a string, a bytes-like object or a number, not 'function'
Is this a bug of Python 3.7?

