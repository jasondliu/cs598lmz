import ctypes
ctypes.cast(my_int_pointer, ctypes.POINTER(ctypes.c_double))
</code>
But this fails with the following error:
<code>TypeError: expected LP_c_double instance instead of LP_c_byte
</code>
Is there a proper way to cast a pointer like this?
If not, is there a way to get a pointer to a specific memory location, and then cast it to a <code>ctypes</code> object?


A:

You can use <code>ctypes.cast</code> to cast a ctypes pointer to another pointer type, but you can't cast an integer to a pointer type.  I'm not sure what you mean by "a pointer to a specific memory location", but it sounds like you just want to get a pointer to a Python object.  In that case, you probably just want to use <code>ctypes.pointer</code>:
<code>p = ctypes.pointer(ctypes.c_double(42.0))
print p.contents.value  # prints 42.0
</code>
If you really need to get the address of an object, you
