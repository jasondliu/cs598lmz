import gc, weakref

class A(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print "A.__del__", self.name

class B(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print "B.__del__", self.name

def f():
    a = A("a")
    b = B("b")
    a.b = b
    b.a = a
    del a
    del b

f()
gc.collect()

a = A("a")
b = B("b")
a.b = b
b.a = a

del a
del b

gc.collect()

a = A("a")
b = B("b")
a.b = b
b.a = a

del a
del b

gc.collect()

a = A("a")
b = B("b")
a.b = b
b.a = a


