import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def func(a, b):
    print "func(%d, %d)" % (a, b)
    return a + b

f = FUNTYPE(func)
print f(1, 2)

# OOP
class Foo(object):
    def __init__(self, x):
        self.x = x
    def bar(self):
        print "Foo.bar()"

f = Foo(10)
print f.x
f.bar()

class Bar(object):
    def __init__(self, x):
        self.x = x
    def bar(self):
        print "Bar.bar()"

b = Bar(20)
print b.x
b.bar()

class Baz(Foo, Bar):
    def __init__(self, x, y):
        Foo.__init__(self, x)
        Bar.__init__(self, y)

b = Baz(30, 40)
print b.
