import ctypes
ctypes.cast(a, ctypes.POINTER(ctypes.c_int))
</code>
This works in Python, but the C function wants a <code>uint32_t*</code>, so I tried passing <code>p</code> to it in the following ways, none of which worked:
<code>ctypes.POINTER(ctypes.c_uint32)
ctypes.POINTER(ctypes.c_int)
ctypes.c_void_p

uint32_t*
int*
void*
</code>
How do I cast <code>a</code> to a <code>uint32_t*</code> so I can call the C function?

