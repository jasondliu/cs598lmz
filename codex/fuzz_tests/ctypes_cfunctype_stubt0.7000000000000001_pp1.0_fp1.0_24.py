import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 123456789
fun()
</code>
Note that the "obvious" solution <code>ctypes.CFUNCTYPE(ctypes.c_long)</code> fails because <code>ctypes.c_long</code> is <code>c_longlong</code> on 64-bit platforms, and Python doesn't know how to convert between <code>c_longlong</code> and <code>long</code>.  You can use
<code>ctypes.CFUNCTYPE(ctypes.c_longlong)
</code>
but it's probably easier to use <code>ctypes.py_object</code> and just let Python do the work.

