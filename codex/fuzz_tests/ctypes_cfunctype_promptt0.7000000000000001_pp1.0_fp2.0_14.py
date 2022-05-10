import ctypes
# Test ctypes.CFUNCTYPE type
def free_func(p):
  p

f = ctypes.CFUNCTYPE(None, ctypes.c_void_p)(free_func)
# Test ctypes.POINTER type
p = ctypes.POINTER(ctypes.c_int)()
# Test ctypes.c_void_p type
p = ctypes.c_void_p()
# Test ctypes.c_char_p type
p = ctypes.c_char_p()
# Test ctypes.c_wchar_p type
p = ctypes.c_wchar_p()
# Test ctypes.py_object type
p = ctypes.py_object()
# Test ctypes.c_int type
p = ctypes.c_int()

# Test ctypes.c_long type
p = ctypes.c_long()
# Test ctypes.c_longlong type
p = ctypes.c_longlong()
# Test ctypes.c_short type
p = ctypes.c_short()
# Test ctypes.c_ushort type

