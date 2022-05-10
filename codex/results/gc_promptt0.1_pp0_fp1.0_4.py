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

foo1_alias = foo1
foo2_alias = foo2
foo3_alias = foo3
foo4_alias = foo4

show_refs('after creating aliases', foo1, foo2, foo3, foo4)

del foo1, foo2, foo3, foo4

show_refs('after deleting aliases', foo1_alias, foo2_alias, foo3_alias
