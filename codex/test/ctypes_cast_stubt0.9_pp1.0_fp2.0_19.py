import ctypes
ctypes.cast(ctypes.create_string_buffer(b'hello world'), ctypes.c_void_p)
