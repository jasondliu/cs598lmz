import gc, weakref

class Object(object):
    pass

class A(Object):
    def __init__(self):
        self.b = B(self)

class B(Object):
    def __init__(self, a):
        self.a = a

a = A()
b = a.b

