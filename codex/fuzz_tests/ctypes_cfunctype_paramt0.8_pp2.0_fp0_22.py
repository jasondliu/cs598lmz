import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

# void set_memory_functions_ptr(void *(*malloc_ptr)(size_t), void *(*calloc_ptr)(size_t, size_t), void *(*realloc_ptr)(void *, size_t), void (*free_ptr)(void *))
malloc_ptr = FUNTYPE(ctypes.c_void_p)
calloc_ptr = FUNTYPE(ctypes.c_void_p)
realloc_ptr = FUNTYPE(ctypes.c_void_p)
free_ptr = FUNTYPE(None)

cfunc = lib.set_memory_functions_ptr
cfunc.argtypes = (malloc_ptr, calloc_ptr, realloc_ptr, free_ptr)
cfunc.restype = None

def set_memory_functions(malloc=None, calloc=None, realloc=None, free=None):
    cfunc(malloc, calloc, realloc, free)

# void set_memory_functions(void *(*malloc_ptr)(size_t), void
