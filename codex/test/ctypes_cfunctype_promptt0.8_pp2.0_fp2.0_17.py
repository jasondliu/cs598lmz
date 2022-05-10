import ctypes
# Test ctypes.CFUNCTYPE
def print_int(i):
    print(i)
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(print_int)
print(cmp_func)
print(cmp_func(5))
# Test ctypes.c_wchar_p
print('ctypes.c_wchar_p')
print(ctypes.sizeof(ctypes.c_wchar_p))
