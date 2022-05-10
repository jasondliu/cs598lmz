import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def fun(x):
    return x+1
func = FUNTYPE(fun)
print(func(10))

# ctypes with class
class MyClass:
    def __init__(self, x):
        self.x = x

    def myfun(self, y):
        return self.x + y

MYFUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
myfun = MYFUNTYPE(MyClass(10).myfun)
print(myfun(1))
