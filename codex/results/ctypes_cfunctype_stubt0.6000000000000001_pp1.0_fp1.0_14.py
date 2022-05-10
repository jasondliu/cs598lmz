import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"

class Foo(object):
    def __init__(self):
        self.fun = fun

def f():
    return Foo()

def main():
    foo = f()
    foo.fun()
    return 0

main()
