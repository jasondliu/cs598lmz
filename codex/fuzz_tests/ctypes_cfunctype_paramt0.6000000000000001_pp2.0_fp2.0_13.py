import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def f(a,b):
    return a+b

fptr = FUNTYPE(f)
fptr(1,2)

#%%
import ctypes

class Test(object):
    def __init__(self):
        self.fptr = None
        self.a = 1
        self.b = 2

    def set_fptr(self, fptr):
        self.fptr = fptr

    def run(self):
        print self.fptr(self.a, self.b)

def g(a,b):
    return a*b

t = Test()
t.set_fptr(FUNTYPE(g))
t.run()
