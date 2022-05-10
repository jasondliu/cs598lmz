import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)
def py_fun(int1,int2):
    return int1+int2

c_fun = FUNTYPE(py_fun)
print(c_fun(1,2))

#类型转换
#python中，每个变量都有一个标签，标签指向这个变量的类型。
#python中的数据类型转换，比如int()，float()，bool()，str()等函数，
# 并非是覆盖了这个变量的值，而只是为这个变量创建了一个新的标
