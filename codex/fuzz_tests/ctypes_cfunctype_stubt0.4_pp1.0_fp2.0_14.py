import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def f():
    return fun

def g():
    return f

def h():
    return g

def main(argv):
    print h()()()
    return 0

def target(*args):
    return main, None

if __name__ == '__main__':
    import sys
    main(sys.argv)
