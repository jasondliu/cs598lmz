import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def make_callback(func):
    return FUNTYPE(func)

def callback(x, y):
    return x + y

cb = make_callback(callback)
print cb(2, 3)

# 使用ctypes模块调用C函数
# 定义一个C函数
# int add(int x, int y) {
#     return x + y;
# }

# 使用ctypes模块调用C函数
# 定义一个C函数
# int add(int x, int y) {
#     return x + y;
# }

# 定义C函数的返回类型和参数类型
# add.restype = ctypes.c_int
# add.argtypes =
