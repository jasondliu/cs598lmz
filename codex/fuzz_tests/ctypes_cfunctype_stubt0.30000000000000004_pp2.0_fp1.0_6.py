import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def fun2():
    return "hello"

print(fun())
print(fun2())
print(fun2.__code__.co_code)
print(fun.__code__.co_code)
print(fun.__code__.co_code == fun2.__code__.co_code)

# 可以看到，fun和fun2的code是一样的，所以可以用fun2的code替换fun的code
fun.__code__ = fun2.__code__
print(fun())

# 可以看到，fun的code已经替换成了fun2的code，所以fun的返回值也变成了fun2的返回值

# 这个技巧可以用来替换函数的
