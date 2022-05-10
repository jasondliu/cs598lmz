import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): return 1
a = fun()
print(a())
</code>
but this seems to raise an <code>AttributeError</code>:
<code>Default arg 2 (canopy.analysis) of callable int cannot be a type</code>
So the more general question is: how can I create a function that returns a function, where I can pass the function arguments?

