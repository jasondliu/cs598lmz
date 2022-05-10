import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

# Test weakref.ref()
class Foo:
    pass

def callback(r):
    print("dead", r)

r = weakref.ref(Foo(), callback)
print(r)

# Test weakref.finalize()
class Foo:
    pass

def callback(r):
    print("dead", r)

f = Foo()
r = weakref.finalize(f, callback, f)
print(r)

# Test weakref.proxy()
class Foo:
    pass

f = Foo()
p = weakref.proxy(f)
print(p)

# Test weakref.WeakKeyDictionary()
class Foo:
    pass

f = Foo()
d = weakref.WeakKeyDictionary()
d[f] = 1
print(d[f])

# Test weakref.WeakValueDictionary()
class Foo:
    pass

f = Foo()
d = weakref.WeakValueDictionary()
d[1] = f
print(d[1])

# Test
