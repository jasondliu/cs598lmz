import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
@FUNTYPE
def func(a, b):
    return a + b
print(func(1, 2))

# 基本类型
# c_bool, c_char, c_wchar, c_byte, c_ubyte, c_short, c_ushort, c_int, c_uint, c_long, c_ulong, c_longlong, c_ulonglong, c_float, c_double, c_longdouble
# 字符串类型
# c_char_p, c_wchar_p, c_void_p

# 数组类型
a = (ctypes.c_int * 3)()
a[0] = 1
a[1] = 2
a[2] = 3
print(a[0], a[1], a[2])

# 结构体类型

