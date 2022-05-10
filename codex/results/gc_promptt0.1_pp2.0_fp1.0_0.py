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
        print('  object %r from %r' % (obj, gc.get_referrers(obj)))

foo1 = Foo('foo1')
foo2 = Foo('foo2')
foo3 = Foo('foo3')
foo4 = Foo('foo4')

show_refs('initial state', foo1, foo2, foo3, foo4)

foo1_ref = weakref.ref(foo1)
foo2_ref = weakref.ref(foo2)
foo3_ref = weakref.ref(foo3)
foo4_ref = weakref.ref(foo4)

show_refs('after weakrefs', foo1, foo2, foo3, foo4)

del foo1, foo2, foo3, foo4
