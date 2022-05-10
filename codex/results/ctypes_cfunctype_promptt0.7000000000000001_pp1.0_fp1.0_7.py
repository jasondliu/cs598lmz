import ctypes
# Test ctypes.CFUNCTYPE on a simple function.

libc = ctypes.CDLL(ctypes.util.find_library("c"))

# int puts(const char *s);
libc.puts.argtypes = ctypes.c_char_p,
libc.puts.restype = ctypes.c_int

# void qsort(void *base, size_t nmemb, size_t size,
#            int (*compar)(const void *, const void *));
libc.qsort.argtypes = ctypes.c_void_p, ctypes.c_size_t, ctypes.c_size_t, \
                      ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p)
libc.qsort.restype = None

# void *bsearch(const void *key, const void *base,
#               size_t nmemb, size_t size,
#               int (*compar)(const void *, const void *));
libc.bsearch.argtypes
