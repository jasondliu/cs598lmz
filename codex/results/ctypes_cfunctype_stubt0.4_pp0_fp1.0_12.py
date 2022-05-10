import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def f():
    return "hello"

def f2():
    return "hello2"

class Test(object):
    def __init__(self):
        self.fun = f2

    def f(self):
        return "hello"

def main():
    print fun()
    print f()
    print f2()
    print Test().f()

if __name__ == '__main__':
    main()
