import ctypes
ctypes.cast(ARRAY_OF_DOUBLE_PTR, ctypes.POINTER(ctypes.ARRAY(ctypes.c_double, len(ARRAY_OF_DOUBLE_PTR)))) # doesn't work
</code>
It throws an error:
<blockquote>
<p>TypeError: expected LP_c_double_Array_2 instance instead of LP_c_double_Array_3</p>
</blockquote>
I can create an instance of it just like this (it seems to work):
<code>POINTER_ARRAY_OF_DOUBLE_PTR = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))
pointer_array_of_double_ptr = (POINTER_ARRAY_OF_DOUBLE_PTR * len(ARRAY_OF_DOUBLE_PTR))()
</code>
However I don't want it to be <code>len(ARRAY_OF_DOUBLE_PTR)</code> long. I want a ctypes pointer to <code>ARRAY_OF_DOUBLE_PTR</code
