import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun_obj = fun()
print(fun_obj)

# 不要这么做
# def fun():
#     return "hello"
#
# fun_obj = FUNTYPE(fun)
# print(fun_obj)

# 2.
# 创建一个C函数指针类型，参数为两个c_int类型，返回值为c_int类型
# c_int_p = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
#
# # 定义一个python函数
# def py_fun(a, b):
#     print("{0} + {1} = {2}".format(a, b, a + b))
#     return a + b
#
# # 将python函
