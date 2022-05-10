import ctypes
# Test ctypes.CFUNCTYPE()

# NOTE: ctypes.CFUNCTYPE(restype, *argtypes)

# int
int_cfunc = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

# void
void_cfunc = ctypes.CFUNCTYPE(None, ctypes.c_int)

# void*: _PTR(void)
ptr_cfunc = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int)

# const void*: _PTR(void)_CONST
const_ptr_cfunc = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int)

# const char*: _PTR(char)_CONST
const_char_ptr_cfunc = ctypes.CFUNCTYPE(ctypes.c_char_p, ctypes.c_int)

# const int*: _PTR(int)_CONST
const_int_ptr_cfunc = ctypes.CFUNCTY
