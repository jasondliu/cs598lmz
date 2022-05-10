import ctypes
# Test ctypes.CFUNCTYPE() with one parameter and a return value
llmemory.cast_ptr_to_adr.argtypes = (ctypes.c_void_p,)
llmemory.cast_ptr_to_adr.restype = ctypes.c_size_t
llmemory.raw_malloc.argtypes = (ctypes.c_size_t,)
llmemory.raw_malloc.restype = ctypes.c_void_p
p = llmemory.raw_malloc(10)
adr = llmemory.cast_ptr_to_adr(p)
_ptr = ctypes.cast(p, ctypes.POINTER(ctypes.c_char))
_ptr[0] = 'A'
_ptr[9] = 'Z'
_ptr[1] = _ptr[0] + 1
_ptr[2] = _ptr[0] + 2
_ptr[3] = _ptr[0] + 3
_ptr[4] = _ptr[0] + 4
_ptr[5] = _ptr[0] + 5
_ptr[6] = _ptr[0] + 6
