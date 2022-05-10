import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

# @functools.wraps(fun)
# def fun():
#     return 1

print(fun())
print(fun.__name__)
print(fun.__doc__)

# print(fun.__module__)
print(fun.__annotations__)

# print(fun.__closure__)
# print(fun.__code__)
# print(fun.__defaults__)
# print(fun.__globals__)
# print(fun.__kwdefaults__)

# print(fun())
# print(fun.__name__)
# print(fun.__doc__)
# print(fun.__module__)
# print(fun.__annotations__)
# print(fun.__closure__)
# print(fun.__code__)
# print(fun.__defaults__)
# print(fun.__globals__)
# print(fun.__kwdefaults__)
