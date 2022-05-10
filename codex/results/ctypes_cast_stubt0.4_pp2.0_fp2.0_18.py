import ctypes
ctypes.cast(ctypes.pointer(x), ctypes.POINTER(ctypes.c_uint32))
</code>
which works.  But I would like to use the <code>ctypes.c_uint32</code> as a template parameter to the <code>cast</code> function, so that it works for any ctypes type.  Is this possible?
I tried
<code>ctypes.cast(ctypes.pointer(x), ctypes.POINTER(ctypes.c_uint32))
</code>
but it doesn't work.


A:

I don't think this is possible.  <code>ctypes.cast</code> is a function, not a class, so it doesn't have a template parameter.  I'm not sure why you would want to do this, but you could always write your own function:
<code>def cast(ptr, type):
    return ctypes.cast(ptr, ctypes.POINTER(type))
</code>

