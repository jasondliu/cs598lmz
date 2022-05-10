import weakref
# Test weakref.ref()

import gc

class Foo:
    pass

def g(x):
    return x

f = Foo()
r = weakref.ref(f, g)

f.foo = 1

gc.collect()

f.foo = 2

gc.collect()

del f

gc.collect()

