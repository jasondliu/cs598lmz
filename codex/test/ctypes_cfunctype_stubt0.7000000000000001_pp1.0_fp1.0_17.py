import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

print(fun())

class A:
    def __init__(self):
        self.a = fun

a = A()
print(a.a())
