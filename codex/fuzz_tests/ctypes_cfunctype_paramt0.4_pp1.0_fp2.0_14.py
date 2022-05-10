import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

@FUNTYPE
def add(a, b):
    return a+b

print(add(1, 2))

# 可以使用ctypes.c_int类型的数组作为参数
def array_fun(n, array):
    for i in range(n):
        array[i] *= array[i]
    return 0

array_type = ctypes.c_int * 5
array = array_type(1, 2, 3, 4, 5)
print(array_fun(5, array))
print(array)

# 可以使用ctypes.c_char_p类型的字符串作为参数
def string_fun(s):
    print(s)
    return 0

s = b'Hello, world!'
string_fun(ctypes.c_char_p(s))

#
