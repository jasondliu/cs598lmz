import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
globals()['zifu']
@fun
def add(a,b):
    return a+b


def fun1():
    return "axiba"

def fun2(arg):
    return arg


@fun1
def test():
    return "xixi"

if __name__ == '__main__':
    print test.__name__
    print test()
    print add(1, 2)
