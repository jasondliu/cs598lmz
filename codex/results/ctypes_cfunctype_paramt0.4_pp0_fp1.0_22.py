import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def py_func(x):
    print(x)
    return x

c_func = FUNTYPE(py_func)
c_func(1)

# 如果想要调用一个函数，需要设置它的参数和返回值类型。
# 如果函数的参数是一个指针，那么在Python中可以传递任何对象，并且会将其转换为指针，并且在调用后，Python会自动释放这个指针。
# 如果函数的
