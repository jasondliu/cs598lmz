import ctypes
# Test ctypes.CFUNCTYPE
func_ptr_type_t = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)
def get_quotes_func_ptr(library_ptr):
    return library_ptr.get_quotes
