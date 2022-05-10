import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect.
gc.collect()

# Test weakref.
class Foo: pass
f = Foo()
r = weakref.ref(f)
print(r)
del f
print(r())
gc.collect()
print(r())

# Test weakref.proxy.
f = Foo()
p = weakref.proxy(f)
print(p)
del f
try:
    print(p)
except ReferenceError:
    pass

# Test weakref.ref.
def callback(r):
    print('callback(', r, ')')
r = weakref.ref(Foo(), callback)
del r
gc.collect()

# Test weakref.proxy.
p = weakref.proxy(Foo(), lambda r: print('callback(', r, ')'))
del p
gc.collect()

# Test weakref.WeakValueDictionary.
d = weakref.WeakValueDictionary()
d[1] = Foo()
print(d[1])
del d[1]
gc.collect()
print(d.get(1))

#
