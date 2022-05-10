import ctypes
ctypes.cast(ctypes.create_string_buffer(b'hello'), ctypes.c_void_p) 
