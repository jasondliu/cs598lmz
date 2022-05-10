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

print(fun2.__code__.co_code == fun.__code__.co_code)
print(fun2.__code__.co_code is fun.__code__.co_code)

print(fun2.__code__.co_code == fun2.__code__.co_code)
print(fun2.__code__.co_code is fun2.__code__.co_code)

print(fun2.__code__.co_code == fun2.__code__.co_code)
print(fun2.__code__.co_code is fun2.__code__.co_code)

print(fun2.__code__.co_code == fun2.__code__.co_code)
print(fun2.__code__.co_code is fun2.__code__.co
