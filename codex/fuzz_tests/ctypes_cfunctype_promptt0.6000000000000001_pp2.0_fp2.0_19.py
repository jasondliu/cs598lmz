import ctypes
# Test ctypes.CFUNCTYPE
c_double_ptr = ctypes.POINTER(ctypes.c_double)
c_double_ptr_ptr = ctypes.POINTER(c_double_ptr)
c_int_ptr = ctypes.POINTER(ctypes.c_int)
c_int_ptr_ptr = ctypes.POINTER(c_int_ptr)

_get_num_threads = ctypes.CDLL('./get_num_threads.so', mode=ctypes.RTLD_GLOBAL)
_get_num_threads.get_num_threads_.argtypes = [ctypes.c_int]
_get_num_threads.get_num_threads_.restype = ctypes.c_int

_set_num_threads = ctypes.CDLL('./set_num_threads.so', mode=ctypes.RTLD_GLOBAL)
_set_num_threads.set_num_threads_.argtypes = [ctypes.c_int]
_set_num_threads.set_num_threads_.
