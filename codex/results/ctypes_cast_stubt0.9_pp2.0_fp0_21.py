import ctypes
ctypes.cast(ctypes.create_string_buffer(b'hello'), ctypes.c_void_p) 
</code>
The function isn't in the standard library, but rather comes from the CPython C extension API, as mentioned here.

