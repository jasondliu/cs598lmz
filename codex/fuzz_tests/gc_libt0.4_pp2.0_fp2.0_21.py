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

print 'a', a.__class__, a.__dict__
print 'b', b.__class__, b.__dict__

print 'a.b', a.b.__class__, a.b.__dict__
print 'b.a', b.a.__class__, b.a.__dict__

del a
print 'a', a.__class__, a.__dict__
print 'b', b.__class__, b.__dict__

print 'a.b', a.b.__class__, a.b.__dict__
print 'b.a', b.a.__class__, b.a.__dict__

gc.collect()

print 'a', a.__class__, a.__dict__
