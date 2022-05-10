import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

class MyClass(object):
    def __init__(self):
        self.my_fun = FUNTYPE(self.my_fun_impl)

    def my_fun_impl(self, a, b):
        return a + b

mc = MyClass()
print(mc.my_fun(1, 2))
</code>

