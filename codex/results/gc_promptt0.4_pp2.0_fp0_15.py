import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def f():
    a = Foo('a')
    w = weakref.ref(a)
    del a
    gc.collect()
    print w()
    return w

w = f()
print w()
del f
gc.collect()
print w()
del w
gc.collect()

# Test gc.collect() with a cyclic trashcan

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def f():
    a = Foo('a')
    b = Foo('b')
    a.other = b
    b.other = a
    del a, b
    gc.collect()

f()

# Test gc.collect() with a cyclic trashcan and a weakref
