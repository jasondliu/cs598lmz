import ctypes
ctypes.cast(ctypes.c_void_p(x), ctypes.POINTER(ctypes.c_int))
</code>
But I get:
<code>TypeError: expected LP_c_int instance instead of pointer to int
</code>
I'm using Python 2.7.2 on Windows 7.
Thanks,


A:

You want <code>ctypes.POINTER(ctypes.c_int)</code>, not <code>ctypes.POINTER(ctypes.c_int)</code>.

