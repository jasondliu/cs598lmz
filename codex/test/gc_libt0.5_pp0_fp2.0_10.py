import gc, weakref

class A(object):
    def __init__(self):
        self.b = B(self)

class B(object):
    def __init__(self, a):
        self.a = weakref.ref(a)

a = A()
a.b

del a
gc.collect()
