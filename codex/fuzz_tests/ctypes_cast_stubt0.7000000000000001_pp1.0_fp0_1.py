import ctypes
ctypes.cast(b'\x00\x00\x00\x00\x00\x00\x00\x00', ctypes.POINTER(ctypes.c_longlong))[0]
</code>

<code>0
</code>

<code>ctypes.cast(b'\x00\x00\x00\x00\x00\x00\x00\x01', ctypes.POINTER(ctypes.c_longlong))[0]
</code>

<code>1
</code>

<code>ctypes.cast(b'\x7f\xff\xff\xff\xff\xff\xff\xff', ctypes.POINTER(ctypes.c_longlong))[0]
</code>

<code>9223372036854775807
</code>

<code>ctypes.cast(b'\x80\x00\x00\x00\x00\x00\x00\x00', ctypes.POINTER(ctypes.c_longlong))[0]
</code>

