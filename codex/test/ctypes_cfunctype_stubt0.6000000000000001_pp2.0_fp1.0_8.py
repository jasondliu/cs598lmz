import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

fun()

class A:
    def __init__(self, name, nb):
        self.name = name
        self.nb = nb

def f(obj):
    print(obj.name, obj.nb)

f(A('joe', 12))

class Foo:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Foo %s>' % self.name

class Bar:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Bar %s>' % self.name

class FooBar:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<FooBar %s>' % self.name

f = FooBar('joe')
def f(obj):
    if isinstance(obj, Foo):
        print('Foo', obj)
   
