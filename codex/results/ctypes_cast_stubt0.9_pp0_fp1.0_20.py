import ctypes
ctypes.cast(ctypes.addressof(y.x), ctypes.POINTER(ctypes.c_int)).contents = 42
print y.x
</code>


A:

You're right. In this case, py2 <code>__safe_for_unpickling__</code> would be the right attribute to use. 
Since you're using py3, maybe <code>__getnewargs_ex__</code> is usable?

