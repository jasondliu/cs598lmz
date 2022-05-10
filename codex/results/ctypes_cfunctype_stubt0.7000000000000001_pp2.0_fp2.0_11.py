import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return b"hello world"

func = fun
print(func())
</code>
This works, but is not very convenient. I would like to use a regular function as the callback, but this is not possible, as the function will return a <code>bytes</code> object.
<code>def fun():
    return b"hello world"
</code>
How can I do this? I would prefer a solution that does not use a class.


A:

You can use a <code>ctypes.CFUNCTYPE</code> as a decorator, with the correct return type specified:
<code>import ctypes

def fun():
    return b"hello world"

FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
func = FUNTYPE(fun)
print(func())
</code>

