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

print r() # prints <__main__.Foo instance at 0x...>

gc.collect()

print r() # prints None

gc.collect()

del r

gc.collect()
