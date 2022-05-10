import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

class Bar:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Bar(%s)' % self.name

def test():
    f = Foo('f')
    b = Bar('b')
    f.b = b
    b.f = f
    del f, b
    gc.collect()

test()

# Test gc.get_referrers()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

class Bar:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Bar(%s)' % self.name

def
