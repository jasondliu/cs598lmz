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

# Create a cycle
f = Foo('f')
b = Foo('b')
f.other = b
b.other = f

show_refs('creating a cycle', f)

# Break the cycle
f.other = None
b.other = None

show_refs('breaking the cycle', f)

# Create a cycle with a dict
d = {}
d[1] = d

show_refs('creating a cycle with a dict', d)

# Create a cycle with a list
l = []
l.append(l)

show_refs('
