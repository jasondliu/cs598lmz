import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)


def py_add(x, y):
    return x + y


add = FUNTYPE(py_add)
print(add(1, 2))

# 将函数指针传递给C
c_add = ctypes.CDLL('./add.so').add
print(c_add(1, 2))

# 将函数指针和参数传递给C
c_add_2 = ctypes.CDLL('./add.so').add_2
c_add_2.argtypes = [FUNTYPE, ctypes.c_int]
c_add_2.restype = ctypes.c_int
print(c_add_2(add, 1))

# 将函数指针返回给Python
c_set_add = ctypes.CDLL('./add.
