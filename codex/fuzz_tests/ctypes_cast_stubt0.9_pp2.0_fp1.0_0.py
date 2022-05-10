import ctypes
ctypes.cast(a,ctypes.c_char_p).value
</code>
You can also try to load the object as a dynamic library and resolve the memory address of the function to obtain a real function pointer. I've done that before with a wrapper I've written, but it was some time ago, and I do not have access to the code at the moment.

