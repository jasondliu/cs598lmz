import ctypes
# Test ctypes.CFUNCTYPE(None, ctypes.c_int), i.e. do not pass a pointer
user_callback_one = ctypes.CFUNCTYPE(None, ctypes.c_int)(lambda x: None)
