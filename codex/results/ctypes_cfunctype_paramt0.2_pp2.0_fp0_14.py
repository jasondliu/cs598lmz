import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback", a, b)
    return a + b

# 将my_callback转换为C回调函数
cb_fun = FUNTYPE(my_callback)

# 将C回调函数传递给C函数
lib.c_callback(cb_fun)

# 调用C函数
lib.c_function()
