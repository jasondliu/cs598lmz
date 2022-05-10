import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int)
def wrapped_function(number):
    return number * 2
fun = FUNTYPE(wrapped_function)
print fun(2)

# ctypes.cast(obj, ctype)的作用是将 ctypes 对象或值 obj 转换成 ctype 类型。
# 前面我们提到 ctypes 对象的类型是 ctypes.c_double，obj 是什么呢？obj 是一个指针，如前面介绍的，我们通过指针保存函数的内存地址，然后在这里通过调用指针得到函数地址
