import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 5
print(fun())
</code>
which correctly prints <code>5</code>. However, when we adjust the return type to <code>int</code> as follows:
<code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
</code>
we get the following:
<code>TypeError: this type has no size
</code>
What does this error mean?


A:

The problem is that <code>c_int</code> is actually a <code>typedef</code> to <code>c_int32</code> and <code>c_int32</code> is not a valid argument to <code>CFUNCTYPE</code> (it is an <code>Object</code> so it has "no size"). 
To fix this, you can use <code>ctypes.POINTER(ctypes.c_int32)</code> instead of <code>ctypes.c_int32</code> (See the Python <code>ctypes</code> documentation).

