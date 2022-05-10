import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

print(fun())
</code>
But the following one fails:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
    return 42

print(FUNTYPE(fun)())
</code>
The error is:
<code>ctypes.ArgumentError: argument 1: &lt;class 'TypeError'&gt;: wrong type
</code>
Why?

