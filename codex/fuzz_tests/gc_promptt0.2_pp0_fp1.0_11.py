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
        print('  referred:', sys.getrefcount(obj))
        print('  refs:', gc.get_referrers(obj))

foo1 = Foo('foo1')
foo2 = Foo('foo2')
foo3 = foo1

show_refs('initial state', foo1, foo2, foo3)

print('collecting...')
n = gc.collect()
print('unreachable objects:', n)
show_refs('after gc', foo1, foo2, foo3)

print('breaking cycles...')
del foo1
del foo2
del foo3
print('collecting...')
n = gc.collect()
print('unreachable objects:', n
