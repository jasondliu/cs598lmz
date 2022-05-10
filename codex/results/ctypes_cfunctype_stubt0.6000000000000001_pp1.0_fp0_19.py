import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "asdf"
</code>
This works as expected.  However, if I try to do this with a list:
<code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(l):
    return l
</code>
I get a segfault.  I have no idea what is going on.  I have tried this with other types, and it seems to be something specific to lists.  For example, this works:
<code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(t):
    return t
</code>
But this doesn't:
<code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object, ctypes.py_object)
@FUNTYPE
def fun(t, l):
    return t
</code>
I've tried using <code>py_object</code> and <code>c_void_
