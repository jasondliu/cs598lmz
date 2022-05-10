import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(a, b):
    print("my_callback called with %d and %d" % (a, b))
    return a + b

my_callback_c = FUNTYPE(my_callback)

my_callback_c(1, 2)

# 使用ctypes.CFUNCTYPE()创建一个函数类型，并使用它来创建一个回调函数。
# 在这个例子中，回调函数接受两个整数参数，并返回一个整数。
# 回调函数的签名必须与FUNTYPE定义的签名相匹配。
