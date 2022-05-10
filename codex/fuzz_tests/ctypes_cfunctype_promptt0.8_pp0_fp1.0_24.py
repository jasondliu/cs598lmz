import ctypes
# Test ctypes.CFUNCTYPE
# From: https://docs.python.org/3/library/ctypes.html#setting-the-argtypes-and-restype-attributes
libc = ctypes.CDLL(ctypes.util.find_library('c'))
strchr = libc.strchr
strchr.argtypes = [ctypes.c_char_p, ctypes.c_char]
strchr.restype = ctypes.c_char_p

buffer = "this is a test"

result = strchr(buffer, ord('t'))
print(result)

result = strchr(buffer, ord('z'))
print(result)
