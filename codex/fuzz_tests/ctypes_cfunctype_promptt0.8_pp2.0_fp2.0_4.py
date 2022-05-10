import ctypes
# Test ctypes.CFUNCTYPE() function
from ctypes import cdll
dll = cdll.LoadLibrary("C:\\Program Files\\Anaconda3\\Scripts\\tests\\ctypes_test.dll")

test_int = ctypes.c_int(7)
test_double = ctypes.c_double(7.7)
test_double_p = ctypes.POINTER(ctypes.c_double)
test_double_pp = ctypes.POINTER(test_double_p)
test_double_ppp = ctypes.POINTER(test_double_pp)

test_int_p = ctypes.POINTER(ctypes.c_int)
test_int_pp = ctypes.POINTER(test_int_p)
test_int_ppp = ctypes.POINTER(test_int_pp)

# 设置dll函数参数类型以及返回值类型
# dll.add_int.argtypes = [ctypes.c_int, ctypes.
