import ctypes
ctypes.cast(None, ctypes.c_void_p)
</code>
Is it possible to call the same function with a NULL argument?


A:

Yes, it is.
You need to use <code>None</code> as the argument (and not <code>0</code> or <code>0L</code> or so).
Then you need to use the <code>_as_parameter_</code> attribute to retrieve the actual value:
<code>ctypes.cast(None, ctypes.c_void_p)._as_parameter_
</code>

If you have a pointer to a structure, you have to use the <code>POINTER</code> type:
<code>a = ctypes.c_int(1)
ctypes.cast(ctypes.byref(a), ctypes.POINTER(ctypes.c_int)).contents.value
1
</code>

