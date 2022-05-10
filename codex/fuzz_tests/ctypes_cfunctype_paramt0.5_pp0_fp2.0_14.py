import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

class Test(object):
    def __init__(self, func):
        self.func = func
        self.func_type = FUNTYPE(self.func)
        self.cfunc = self.func_type(self.func)

    def run(self):
        print(self.cfunc(1))

def func(x):
    return x + 1

t = Test(func)
t.run()
</code>

