import ctypes
ctypes.cast(ptr_to_ptr, ctypes.POINTER(ctypes.c_char_p))
</code>
That is, you need to create a <code>POINTER</code> to <code>c_char_p</code>, not to <code>c_char</code>.

