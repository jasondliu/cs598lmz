import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass
fun = fun
</code>
This works, but it isn't very pretty.  Is there a more elegant way to store a <code>ctypes.CFUNCTYPE</code> in a variable?


A:

<code>import ctypes

FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
fun = FUNTYPE(lambda: None)
</code>

