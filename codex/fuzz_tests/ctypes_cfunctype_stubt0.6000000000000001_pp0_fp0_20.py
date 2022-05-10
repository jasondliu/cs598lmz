import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

obj = fun()
print(obj)
print(type(obj))
print(type(fun))
print(fun)

#todo: 为什么这样就能让我们在动态库中声明一个返回值是PyObject的函数，可以在Python中调用，返回PyObject？

"""
答案：

"""

"""
    #todo: 这里我们又回到了第一个问题，动态库中为什么要用PyObject，这里我们又回到了第一个问题，动态库中为什么要用PyObject。
    #todo:
