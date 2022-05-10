import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo(' + self.name + ')'

def show_refs(message, *objects):
    print(message)
    for obj in objects:
        print('  object:', obj)
        print('  refcount:', sys.getrefcount(obj))
        print('  referrers:', gc.get_referrers(obj))

a = Foo('a')
b = Foo('b')
c = Foo('c')

show_refs('initial:', a, b, c)

a = b = c = None

show_refs('collected:', gc.collect())

a = Foo('a')
b = Foo('b')
c = Foo('c')

show_refs('created:', a, b, c)

del a, b, c

show_refs('deleted:', gc.collect())

# Test gc.garbage
