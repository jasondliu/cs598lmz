import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(%s)' % self.name

def show_refs(message, *objects):
    print(message)
    for obj in objects:
        print('  object %r from %r' % (obj, obj.__class__))
        print('  referrers:', repr(gc.get_referrers(obj)))

a = Foo('a')
b = Foo('b')
c = Foo('c')

show_refs('initial:', a, b, c)

a = None
b = None
c = None

show_refs('collected:', gc.collect())

# Test weakref.ref()

class ExpensiveObject:
    def __del__(self):
        print('(Deleting %s)' % self)

obj = ExpensiveObject()
r = weakref.ref(obj)

print('obj:', obj)
print('ref:
