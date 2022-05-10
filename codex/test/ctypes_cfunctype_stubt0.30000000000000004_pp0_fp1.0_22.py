import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())

# 可以用ctypes.cast将一个函数转换为另一个函数类型，但是这个函数必须是C风格的，
# 也就是说，它的参数和返回值必须是C的基本类型或者是指针。

# 如果想要把一个Python函数转换为一个C函数，可以使用ctypes.pythonapi.PyCFunction_NewEx()。
# 这个函数的第一个参数是一个Python函数对象，第二个
