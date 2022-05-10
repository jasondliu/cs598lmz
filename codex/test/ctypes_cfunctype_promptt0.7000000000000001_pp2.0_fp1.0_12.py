import ctypes
# Test ctypes.CFUNCTYPE
def func_cdecl(a, b, c):
    return ctypes.c_int(a + b + c)
func_cdecl.restype = ctypes.c_int
func_cdecl.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]

def func_stdcall(a, b, c):
    return ctypes.c_int(a + b + c)
func_stdcall.restype = ctypes.c_int
func_stdcall.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]

def func_fastcall(a, b, c):
    return ctypes.c_int(a + b + c)
func_fastcall.restype = ctypes.c_int
func_fastcall.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]

