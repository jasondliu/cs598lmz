import ctypes
# Test ctypes.CFUNCTYPE

libc = ctypes.CDLL(ctypes.util.find_library("c"))

# prototype of printf() is:
# int printf(const char *format, ...);
PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

printf = PROTOTYPE(("printf", libc))

printf("hello, world\n")

# prototype of strlen() is:
# size_t strlen(const char *s);
PROTOTYPE = ctypes.CFUNCTYPE(ctypes.c_size_t, ctypes.c_char_p)

strlen = PROTOTYPE(("strlen", libc))

print("strlen('hello, world') =", strlen("hello, world"))

# prototype of free() is:
# void free(void *ptr);
PROTOTYPE = ctypes.CFUNCTYPE(None, ctypes.c_void_p)

free = PROTOTYPE(("free", libc))

