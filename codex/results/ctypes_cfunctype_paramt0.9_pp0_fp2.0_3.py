import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)
print(type(Foo.obj))
print(type(Foo.obj_wo_type))
print(Foo.func)
print(type(Foo.func))
print(type(Foo.func_wo_type))

print(Foo.obj(1.0, 1.0))
print(Foo.obj_wo_type(1.0, 1.0))
print(Foo.func(1.0, 1.0))
print(Foo.func_wo_type(1.0, 1.0))
