import ctypes
# Test ctypes.CFUNCTYPE and ctypes.c_void_p
if sys.platform=='win32':
    libm = ctypes.cdll.msvcrt
else:
    libm = ctypes.cdll.LoadLibrary(find_library('m'))
CMPFUNC = ctypes.CFUNCTYPE( ctypes.c_int, ctypes.c_void_p, ctypes.c_void_p )

libc = ctypes.CDLL(find_library('c'))
qsort = libc.qsort
qsort.argtypes = ( ctypes.c_void_p, # void*, base
                   ctypes.c_size_t, # size_t, nmemb
                   ctypes.c_size_t, # size_t, size,
                   CMPFUNC)          # int(*),  cmp

def compare_sizes(a, b):
    astr = ctypes.c_char_p(a, 1)
    bstr = ctypes.c_char_p(b, 1)
    return cmp(len(
