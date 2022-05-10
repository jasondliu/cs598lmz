import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

class A(object):
    def __init__(self):
        self.f = fun

class B(object):
    def __init__(self):
        self.f = fun

a = A()
b = B()

def main():
    print a.f()
    print b.f()

main()
