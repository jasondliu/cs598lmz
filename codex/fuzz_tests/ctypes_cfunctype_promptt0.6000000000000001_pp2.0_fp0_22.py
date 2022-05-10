import ctypes
# Test ctypes.CFUNCTYPE()

import ctypes

# int puts(const char *s);
libc = ctypes.CDLL(ctypes.util.find_library("c"))
puts = libc.puts
puts.restype = ctypes.c_int
puts.argtypes = [ctypes.c_char_p]

# void (*)(const char *)
CMPFUNC = ctypes.CFUNCTYPE(None, ctypes.c_char_p)

def my_puts(s):
    puts(s)

# int qsort(void *base, size_t nmemb, size_t size,
#           int (*compar)(const void *, const void *));
libc.qsort.restype = None
libc.qsort.argtypes = [ctypes.c_void_p, ctypes.c_size_t,
                       ctypes.c_size_t, CMPFUNC]

# int strcmp(const char *s1, const char *s2);
libc.strcmp.restype = ctypes.
