import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return '123'

print(fun())
</code>
<blockquote>
<p>ReferenceError: value is not defined</p>
</blockquote>

