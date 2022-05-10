import ctypes
# Test ctypes.CFUNCTYPE()
ctypes.CFUNCTYPE(None)

# cpdef void* PyMem_Malloc(size_t n)

PyMem_Malloc = libpython.PyMem_Malloc
PyMem_Malloc.restype = ctypes.c_void_p
PyMem_Malloc.argtypes = [ctypes.c_size_t]

# cpdef void PyMem_Free(void *p)
PyMem_Free = libpython.PyMem_Free
PyMem_Free.restype = None
PyMem_Free.argtypes = [ctypes.c_void_p]

# cpdef void* PyMem_Realloc(void* p, size_t n)
PyMem_Realloc = libpython.PyMem_Realloc
PyMem_Realloc.restype = ctypes.c_void_p
PyMem_Realloc.argtypes = [ctypes.c_void_p, ctypes.c_size_t]

# cpdef void* PyMem_Calloc(size_t nelem, size_t elsize)
PyMem_
