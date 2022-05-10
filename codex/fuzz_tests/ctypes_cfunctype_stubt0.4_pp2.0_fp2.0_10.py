import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"

print(fun())

# 函数对象
def fun(x):
    return x + 1

print(fun(2))
print(fun.__name__)
print(fun.__code__)
print(fun.__code__.co_varnames)
print(fun.__code__.co_argcount)

# 函数的高阶用法: 函数作为参数
def apply_fun(fun, arg):
    return fun(arg)

print(apply_fun(fun, 3))

# 函数的高阶用法: 函数作为返回值
def make_fun(x):
    def inner_fun():
        return x
    return inner_fun

f = make_fun(3)
print(f())

# 函数的高阶用法: 函数作为
