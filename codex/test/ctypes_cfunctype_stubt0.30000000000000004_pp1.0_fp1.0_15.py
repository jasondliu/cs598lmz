import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World"

print(fun())

# 使用ctypes.CFUNCTYPE创建一个函数类型，这里的函数类型是指返回值是ctypes.py_object类型，参数为空的函数类型。
# 使用@ctypes.CFUNCTYPE装饰器将函数类型作为参数传递给函数fun，这样函数fun就变成了一个函数类型的函数，
# 可以直接调用。

# 创建一个函数类型，这里的函
