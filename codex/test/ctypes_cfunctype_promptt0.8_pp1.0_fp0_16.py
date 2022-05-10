import ctypes
# Test ctypes.CFUNCTYPE(...) for a function pointer.
import ctypes

def use_func(func):
    res = func(1, 2)
    if res != 3:
        raise RuntimeError("res should be 3")

# With ctypes, the ctypes.POINTER type is used to get a pointer type.
MyFuncType = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
MyFunc = MyFuncType(lambda a, b: a + b)
use_func(MyFunc)

# With cffi, the ffi.typeof('int(*)(int, int)') is used to get a pointer type.
