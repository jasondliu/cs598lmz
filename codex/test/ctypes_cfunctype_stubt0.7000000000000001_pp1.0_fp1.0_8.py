import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

# fun()
# TypeError: 'int' object is not callable

class C:
    pass
c = C()
c.fun = FUNTYPE(fun)
print(c.fun())
# 42
