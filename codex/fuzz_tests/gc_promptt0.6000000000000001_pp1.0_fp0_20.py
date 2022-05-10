import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def f():
    a = weakref.WeakKeyDictionary()
    a[{}] = 1
    return a

print(f())
gc.collect()
print(gc.garbage)
# Test gc.collect() with cyclic garbage
def f():
    a = weakref.WeakKeyDictionary()
    a[{}] = 1
    return a

print(f())
gc.collect()
print(gc.garbage)
# Test gc.collect() with cyclic garbage that is not collectable
def f():
    a = weakref.WeakKeyDictionary()
    a[{}] = 1
    return a

print(f())
gc.collect()
print(gc.garbage)
# Test gc.get_referrers()
def f():
    a = weakref.WeakKeyDictionary()
    a[{}] = 1
    return a

print(f())
print(gc.get_referrers(a))
gc.collect()
print(gc.garbage)
# Test gc.get_
