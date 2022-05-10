import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello"

class MyType(type):
    def __new__(cls, name, bases, attrs):
        return super(MyType, cls).__new__(cls, name, bases, attrs)
    def __call__(self, *args, **kwargs):
        print('MyType __call__')
        return super(MyType, self).__call__(*args, **kwargs)

class MyObj(object):
    __metaclass__ = MyType
    def __new__(cls, *args, **kwargs):
        print('MyObj __new__')
        return super(MyObj, cls).__new__(cls, *args, **kwargs)
    def __init__(self, *args, **kwargs):
        print('MyObj __init__')
        super(MyObj, self).__init__(*args, **kwargs)

print('start')
o = MyObj()

class Test(object):
    def __new__(cls, *args, **kwargs):
        print
