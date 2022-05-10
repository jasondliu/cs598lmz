import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World"

a = fun()
print(a)

# 函数指针
print("函数指针")
print(fun)
print(type(fun))
print(fun.__class__)
print(fun.__code__.co_name)
print(fun.__code__.co_argcount)
print(fun.__code__.co_varnames)
print(fun.__code__.co_consts)
print(fun.__code__.co_code)
print(fun.__code__.co_nlocals)
print(fun.__code__.co_stacksize)
print(fun.__code__.co_flags)
print(fun.__code__.co_firstlineno)
print(fun.__code__.co_lnotab)

# 函数指针的字符串表示
print("函数指针的字符
