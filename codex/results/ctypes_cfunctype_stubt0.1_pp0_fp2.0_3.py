import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def fun2():
    return "hello"

print(fun())
print(fun2())

print(type(fun))
print(type(fun2))

print(fun.__name__)
print(fun2.__name__)

print(fun.__code__)
print(fun2.__code__)

print(fun.__code__.co_code)
print(fun2.__code__.co_code)

print(fun.__code__.co_consts)
print(fun2.__code__.co_consts)

print(fun.__code__.co_varnames)
print(fun2.__code__.co_varnames)

print(fun.__code__.co_argcount)
print(fun2.__code__.co_argcount)

print(fun.__code__.co_flags)
print(fun2.__code__.co_flags)

print(fun.__code__.co_names)
print(fun2.__code
