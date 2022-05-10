import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

@FUNTYPE
def add(x, y):
    return x + y

print(add(1, 2))

# 将C语言的函数指针传给Python
def my_callback(x, y):
    return x + y

my_callback = FUNTYPE(my_callback)
print(add(1, 2))

# 将Python的函数指针传给C
add = FUNTYPE(add)
print(add(1, 2))

# 将Python的函数指针传给C
add = FUNTYPE(add)
print(add(1, 2))

# 将Python的函数指针传给C
add = FUNTYPE(add)
print(add(1, 2))

# 将Python的函数指
