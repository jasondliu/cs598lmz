import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): 
    ... 
ctypes.cast(fun, ctypes.py_object)
</code>
The id of <code>ctypes.cast(fun, ctypes.py_object)</code> and <code>fun</code> is different, by the way.
How to coerce a PyCFunctionObject to a PyObject?


A:

<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): 
    ... 
ctypes.py_object(fun)
</code>
You can construct a <code>ctypes.py_object</code>, which is a pointer, from anything that is an <code>object</code> in C++ land.  Python functions are such.

