import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def foo(a, b):
    print("Python: foo({}, {})".format(a, b))
    return a + b

# cfunc = FUNTYPE(foo)
cfunc = FUNTYPE(lambda a, b: a + b)
print(cfunc)
print(cfunc(1, 2))
print(ctypes.c_int(1).value)
