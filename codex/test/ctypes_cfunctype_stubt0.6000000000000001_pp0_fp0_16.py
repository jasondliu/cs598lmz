import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    if False:
        yield
    return 42

def f():
    return fun()

def g():
    return f()

def main():
    print(g()())
    print(g()())
    print(g()())
    print(g()())
    print(g()())
    print(g()())
    print(g()())
    print(g()())
    print(g()())
    print(g()())
    print(g()())
    print(g()())
    print(g()())
    print(g()())
    print(g()())
    print(g()())
    print(g()())
    print(g()())
    print(g()())
    print(g()())

