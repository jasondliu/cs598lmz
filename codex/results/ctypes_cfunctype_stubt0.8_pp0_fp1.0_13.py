import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print('fun called')
    return num


class MyClass(object):
    """docstring for MyClass"""
    def __init__(self, arg):
        super(MyClass, self).__init__()
        self.arg = arg

def fun2():
    print('fun2 called')
    return MyClass(0)

if __name__ == '__main__':
    def test(fun):
        print(fun())
    test(fun)
    test(fun2)
