import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Create some classes, to create some GC-monitored objects.
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


# Create some objects, and trigger the monitoring of them
a = Foo('a')
b = Foo('b')
a.other = b
b.other = a
a_r = weakref.ref(a)
b_r = weakref.ref(b)
a_r2 = weakref.ref(a)
b_r2 = weakref.ref(b)
assert a_r() is a
assert b_r() is b

class A(object):
    def x(self): pass
    def y(self): pass
    def z(self): pass

class
