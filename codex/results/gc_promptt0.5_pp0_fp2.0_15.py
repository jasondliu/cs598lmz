import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

class Bar(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Bar(%s)' % self.name

class FooBar(object):
    def __init__(self, name):
        self.name = name
        self.foos = [Foo(name+str(i)) for i in range(10)]

f = FooBar('f')
b = Bar('b')
f.b = b
b.f = f

def test():
    f = FooBar('f')
    b = Bar('b')
    f.b = b
    b.f = f
    del f, b
    gc.collect()

test()

# Test gc.get_referents()

# Test gc.get_referrers(obj
