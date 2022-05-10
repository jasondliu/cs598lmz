import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "fun"

def f(x):
    return x

def g(x):
    return 2*x

def apps(fs, *xs):
    if(len(xs) == 0):
        raise Exception("apps: no function")
    if(len(xs) == 1):
        return fs[0](xs[0])
    return apps(fs[1:], *(fs[0](*xs)))

def tests():
    print("tests")
    assert fun() == "fun"
    assert apps((f,g),2) == 4
    assert apps((f,g),f,g,f,g,2) == 16

if __name__ == "__main__":
    tests()
