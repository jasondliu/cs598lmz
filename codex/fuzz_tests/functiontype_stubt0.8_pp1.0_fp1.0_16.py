from types import FunctionType
a = (x for x in [1])
b = lambda x: x
c = 10
d = map
e = FunctionType

class X(object):
    def __init__(self):
        self.foo = 1

x = X()

def f():
    pass

f.x = x

print f.x.foo

def check_type(func):
    if isinstance(func, FunctionType):
        print func.__name__, 'is a function'
    elif isinstance(func, (int, float, str, tuple, list)):
        print func, 'is a literal'
    elif isinstance(func, type):
        print func.__name__, 'is a type'
    elif isinstance(func, type(a)):
        print 'generator'
    elif isinstance(func, (type(d), type(e))):
        print func.__name__, 'is a built-in'
    elif isinstance(func, type(x)):
        print 'instance'
    else:
        print 'dunno'

check_type
