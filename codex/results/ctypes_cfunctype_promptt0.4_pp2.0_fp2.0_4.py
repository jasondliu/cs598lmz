import ctypes
# Test ctypes.CFUNCTYPE()

import ctypes

@ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def func(x):
    print(x)
    return x + 1

func(1)
func(2)
func(3)

print(func.__name__)
print(func.__doc__)
print(func.__module__)
print(func.__dict__)
print(func.__defaults__)
print(func.__code__)
print(func.__globals__)
print(func.__closure__)
print(func.__annotations__)

print(func.__class__)
print(func.__class__.__name__)

print(func.__bases__)
print(func.__bases__[0].__name__)

print(func.__mro__)
print(func.__mro__[0].__name__)
print(func.__mro__[1].__name__)
print(func.__mro__[
