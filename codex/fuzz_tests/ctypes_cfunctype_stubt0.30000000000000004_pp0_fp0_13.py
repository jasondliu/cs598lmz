import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def f():
    return fun()

def g():
    return f()

def h():
    return g()

def main():
    for i in range(100):
        h()

main()
