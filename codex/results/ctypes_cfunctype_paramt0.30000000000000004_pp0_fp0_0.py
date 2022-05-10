import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(x, y):
    return x + y

func_ptr = FUNTYPE(func)
print(func_ptr(1, 2))

# 将函数指针赋值给一个变量
func_ptr2 = func_ptr
print(func_ptr2(2, 3))

# 将函数指针作为参数传递给另一个函数
def func2(x, y, func_ptr):
    return func_ptr(x, y)

print(func2(3, 4, func_ptr))

# 将函数指针作为返回值返回
def func3():
    return func_ptr

func_ptr3 = func3()
print(func_ptr3(4, 5))
