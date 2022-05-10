import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass

class C:
    def __init__(self):
        self.f = fun

c = C()

def f():
    return c.f

def g():
    return f()

def h():
    return g()

def main():
    f()
    g()
    h()

main()
