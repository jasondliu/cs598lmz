import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

@FUNTYPE
def func(a, b, c):
    print 'func(%d, %d, %d)' % (a, b, c)
    return a * 100 + b * 10 + c

class Test(object):
    def __init__(self, p):
        self.p = p

    def __call__(self, a, b, c):
        print 'Test(%d, %d, %d)' % (a, b, c)
        return a * 100 + b * 10 + c

def py_func(a, b, c):
    print 'py_func(%d, %d, %d)' % (a, b, c)
    return a * 100 + b * 10 + c

if __name__ == '__main__':
    test = Test(func)
    print test.p(1,2,3)
    print test(1,2,3)
