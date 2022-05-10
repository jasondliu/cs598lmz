import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def show_refs(message, *objects):
    print message
    for obj in objects:
        print '  object %r from %r' % (obj, obj.__class__)
        print '  referrers:', gc.get_referrers(obj)

a = Foo('a')
b = Foo('b')
show_refs('initial:', a, b)

a.other = b
b.other = a
show_refs('linked:', a, b)

del a
del b
gc.collect()
show_refs('collected:', Foo.__dict__.values())

# Test gc.get_referrers()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' %
