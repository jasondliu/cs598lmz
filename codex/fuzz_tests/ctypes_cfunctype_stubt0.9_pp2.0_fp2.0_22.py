import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'success'
    
lib.fun.restype = ctypes.py_object
res = lib.fun()
print res
</code>
Running that code gives
<code>PyObject&lt;class 'str'&gt;: success
</code>
and after that you can do what you want with <code>res</code>.

