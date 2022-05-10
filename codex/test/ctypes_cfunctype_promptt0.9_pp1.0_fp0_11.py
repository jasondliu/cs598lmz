import ctypes
# Test ctypes.CFUNCTYPE 
def call_callback(f, arg):
    print(arg)

callback_type = ctypes.CFUNCTYPE(None, ctypes.c_char_p)

instance = callback_type(call_callback)
