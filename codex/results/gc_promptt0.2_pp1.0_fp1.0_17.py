import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def bar():
    print('in bar')
    f = Foo()
    wr = weakref.ref(f, bar)
    print('leaving bar')

bar()
gc.collect()
print('end of test')
