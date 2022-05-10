import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.y = f

print(gc.collect())
# Test gc.get_objects()

import gc

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.y = f

print(len(gc.get_objects()))
# Test gc.get_stats()

import gc

gc.set_debug(gc.DEBUG_STATS)

class Foo:
    pass

f = Foo()
f.x = Foo()
f.x.y = f

print(gc.get_stats())
# Test gc.get_threshold()

import gc

print(gc.get_threshold())
# Test gc.set_threshold()

import gc

gc.set_threshold(10, 10, 10)

print(gc.get_threshold())
# Test gc.is_tracked()

import gc

class Foo:

