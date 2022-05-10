import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

# print('fun() : ', fun())
# print('fun() : ', repr(fun()))
# print('fun() : ', hex(id(fun())))
# print('fun() : ', type(fun()))


@FUNTYPE
def fun2(func):
    return func

print(fun2(fun))

# from ctypes import CFUNCTYPE, py_object
# ADDTYPE = CFUNCTYPE(py_object, py_object, py_object)
# def add(a, b):
#     return a + b
#
# add_fun = ADDTYPE(add)
# print(add_fun(1, 2))
#
# minus_fun = ADDTYPE(lambda a, b : a - b)
# print(minus_fun(1, 2))

# ******* 所以把python的函数叫fun-object，把c的函数叫fun-descriptor

# ******* python 内置的函数求
