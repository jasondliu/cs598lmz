import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

print(fun())

class C:
    pass

c = C()
c.f = FUNTYPE(fun)
c.f()
