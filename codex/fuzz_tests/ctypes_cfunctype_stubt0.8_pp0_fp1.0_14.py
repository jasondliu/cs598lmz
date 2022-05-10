import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

print("fun.__code__.co_freevars",fun.__code__.co_freevars)
print("fun.__closure__",fun.__closure__)

@FUNTYPE
def fun2(a:int, b:int)->int:
    return a + b

@FUNTYPE
def fun3(a, b):
    return a + b

print("fun3.__annotations__",fun3.__annotations__)

print("fun2(1,2)", fun2(1,2))
print("fun3(1,2)", fun3(1,2))
