import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class A:
    def __init__(self):
        self.b = B(self)
        print 'A: self:', repr(self), 'b:', repr(self.b)

class B(object):
    def __init__(self, a):
        self.a = a
        print 'B: self:', repr(self), 'a:', repr(self.a)

gc.collect()
print 'creating A'
a = A()
print 'getting b'
b = a.b
print 'deleting a'
del a
print 'deleting b'
del b
print 'calling gc'
gc.collect()

class A:
    def __init__(self):
        self.b = B(self)
        print 'A: self:', repr(self), 'b:', repr(self.b)

class B(object):
    def __init__(self, a):
        self.a = a
        print 'B: self:', repr(self), 'a:', repr(self.a)
