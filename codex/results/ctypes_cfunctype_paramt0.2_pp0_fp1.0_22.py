import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback", a, b)
    return a + b

my_callback_c = FUNTYPE(my_callback)

print(my_callback_c(1, 2))

# 回调函数的使用
# 回调函数的使用
# 回调函数的使用
# 回调函数的使用
# 回调函数的使用
# 回调函数的使用
# 回调函数的使用
# 回调函数的使用
# 回调函数的使用
# 回调函数的使用
# 回调函数的使
