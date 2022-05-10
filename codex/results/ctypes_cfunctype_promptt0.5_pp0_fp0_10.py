import ctypes
# Test ctypes.CFUNCTYPE()

# A simple function
def _func_type(arg):
    return arg

# A simple function that takes a pointer as argument
def _func_ptr(arg):
    return ctypes.cast(arg, ctypes.c_char_p).value

# A simple function that takes a pointer as argument and returns a pointer
def _func_ptr_ptr(arg):
    return ctypes.cast(arg, ctypes.c_void_p)

# A simple function that takes a pointer as argument and returns a pointer
def _func_ptr_ptr_ref(arg):
    return ctypes.byref(arg)

# A simple function that takes a pointer as argument and returns a pointer
def _func_ptr_ptr_ref_ref(arg):
    return ctypes.byref(ctypes.byref(arg))

# A simple function that takes a pointer as argument and returns a pointer
def _func_ptr_ptr_ref_ref_ref(arg):
    return ctypes.byref(ctypes.byref(ctypes.byref(arg)))

# A
