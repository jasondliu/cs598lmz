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
        print('  referred:', sys.getrefcount(obj))
        print('  weakrefs:', list(weakref.getweakrefs(obj)))

a = Foo('a')
b = Foo('b')
c = Foo('c')

show_refs('initial:', a, b, c)

a_wr = weakref.ref(a)
b_wr = weakref.ref(b)
c_wr = weakref.ref(c)

show_refs('created weakrefs:', a, b, c)

del a
del b
del c

gc.collect()

show_refs('after gc:', a_wr, b_wr, c_wr
