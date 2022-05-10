import ctypes
ctypes.cast(my_var, ctypes.c_char_p).value

# We can also do the same thing with ctypes.c_char. This will also ensure that we get the bytes as they are.
my_var = b'Hello'
ctypes.cast(ctypes.pointer(ctypes.c_char.from_buffer(my_var)), ctypes.c_char_p).value
</code>

