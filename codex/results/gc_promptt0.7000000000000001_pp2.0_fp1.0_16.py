import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
print(gc.collect())

class Foo(object): pass
f = Foo()
r = weakref.ref(f)
print(r)

del f
print(gc.collect())
print(r)

# Test gc.get_referrers()
import gc

class Foo(object): pass
f = Foo()
x = [f]
g = {'foo':f}

print(gc.get_referrers(f))

# Test gc.get_threshold()
import gc

print(gc.get_threshold())

# Test gc.get_count()
import gc

print(gc.get_count())

# Test gc.set_threshold()
import gc

print(gc.set_threshold(10, 10, 10))

# Test gc.debug()
import gc

print(gc.set_debug(gc.DEBUG_LEAK))

# Test gc.is_tracked()
import gc

f = []
print(gc.is_tr
