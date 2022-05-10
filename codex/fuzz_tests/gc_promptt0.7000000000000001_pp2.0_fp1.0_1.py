import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() after weakref creation
class Foo:
    def __del__(self):
        print('Foo dying')

def get_weakref(f):
    return weakref.ref(f)

def no_weakref(f):
    pass

f = Foo()
print('\nRunning tests with gc.disable()')
gc.disable()
for t in (get_weakref, no_weakref):
    print('\nTesting', t)
    t(f)
    f2 = f
    f = None
    gc.collect()
    print('f2:', f2 is None)
del f2
print('\nRunning tests with gc.enable()')
gc.enable()
for t in (get_weakref, no_weakref):
    print('\nTesting', t)
    t(f)
    f2 = f
    f = None
    gc.collect()
    print('f2:', f2 is None)
