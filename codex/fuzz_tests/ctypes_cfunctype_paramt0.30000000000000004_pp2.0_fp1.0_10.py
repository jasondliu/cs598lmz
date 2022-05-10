import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def pyfunc(x):
    return x * x

cfunc = FUNTYPE(pyfunc)

print(cfunc(10))

# 使用ctypes.CFUNCTYPE()创建一个可调用的C函数类型，参数为返回值类型和参数类型的元组。
# 使用ctypes.CFUNCTYPE()创建的函数类型可以像函数一样调用，参数为参数类型的元组。
# 这里的pyfunc()是一个Python函数，它的返回值类型为int，
