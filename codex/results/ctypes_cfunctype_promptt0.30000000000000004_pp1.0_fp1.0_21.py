import ctypes
# Test ctypes.CFUNCTYPE

def func(a, b):
    return a + b

def func_ptr(a, b):
    return func(a, b)

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
ptr = CALLBACK(func_ptr)

print(ptr(1, 2))

print(ptr.__name__)
print(ptr.__qualname__)
print(ptr.__module__)
print(ptr.__doc__)
print(ptr.__text_signature__)
print(ptr.__annotations__)
print(ptr.__dict__)
print(ptr.__class__)
print(ptr.__code__)
print(ptr.__defaults__)
print(ptr.__closure__)
print(ptr.__globals__)
print(ptr.__dict__)
print(ptr.__name__)
print(ptr.__qualname__)
print(ptr.__module__)
print(ptr.__doc__)

