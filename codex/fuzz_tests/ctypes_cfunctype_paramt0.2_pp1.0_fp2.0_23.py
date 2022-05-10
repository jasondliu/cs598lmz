import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    return a + b

f = FUNTYPE(func)
print(f(1, 2))

# 将函数指针作为参数传递
def func2(f, a, b):
    return f(a, b)

print(func2(f, 2, 3))

# 将函数指针作为返回值返回
def func3():
    return f

f2 = func3()
print(f2(3, 4))

# 将函数指针作为元素存储在数组中
array = (FUNTYPE * 2)(f, f)
print(array[0](4, 5))
print(array[1](5, 6))

# 将函数指
