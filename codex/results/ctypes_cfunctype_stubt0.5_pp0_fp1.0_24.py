import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
</code>
This gives the following error:
<code>TypeError: 'CFUNCTYPE' object is not subscriptable
</code>
So, I tried the following:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE()
def fun():
    return "hello"
</code>
This gives the following error:
<code>TypeError: 'CFUNCTYPE' object is not callable
</code>
So, I tried the following:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
fun = FUNTYPE(fun)
</code>
This gives the following error:
<code>TypeError: 'CFUNCTYPE' object is not callable
</code>
So, I tried the following:
<code>import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
   
