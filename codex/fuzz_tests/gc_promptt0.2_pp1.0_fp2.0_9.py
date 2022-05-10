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
        print('  object:', obj)
        print('  refcount:', sys.getrefcount(obj))
        print('  referrers:', gc.get_referrers(obj))

a = Foo('a')
b = Foo('b')
c = Foo('c')

show_refs('initial:', a, b, c)

a_ref = weakref.ref(a)
b_ref = weakref.ref(b)
c_ref = weakref.ref(c)

show_refs('refs created:', a, b, c)

del a
del b
del c

gc.collect()

show_refs('after collect:', a_ref, b_ref, c_ref)


