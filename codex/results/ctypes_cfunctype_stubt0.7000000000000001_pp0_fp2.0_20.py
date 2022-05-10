import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

def f(x):
    return 0

def g(x):
    return 1

def check(f):
    for i in range(10):
        f()

def main():
    check(fun)
    check(f)
    check(g)

main()
