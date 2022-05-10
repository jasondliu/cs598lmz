import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_int, ctypes.POINTER(ctypes.c_double))

def create_func(func):
    return FUNTYPE(func)

def create_func_from_source(source):
    return create_func(create_func_from_source.module.__dict__[source])

create_func_from_source.module = imp.new_module('temp')

@create_func
def func(x, y):
    return x**2 + y**2

@create_func_from_source
def func2(x, y):
    return x**2 + y**2

create_func_from_source.module.func2 = func2
print(func(1, 2))
print(func2(1, 2))
print(func2.__module__)
</code>

