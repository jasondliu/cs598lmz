import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
print gc.collect()

# Test weakrefs
a = {1, 2, 3}
w = weakref.WeakKeyDictionary()
w['a'] = 1
w[a] = 2
print w
print w.items()
print w['a']
print w[a]
del a
gc.collect()
print w.items()

# Test circular garbage
a = {}
a[0] = a
del a
gc.collect()

# Test finalizers
class A:
    def __del__(self):
        print 'del A'

a = A()
b = A()
a.b = b
b.a = a
del a
del b
gc.collect()

# Test __del__ with an exception
class A:
    def __del__(self):
        raise Exception

def g():
    a = A()
    a.b = a
    a.a = a
    del a
    del a
    gc.collect()

try:
    g()
except Exception:

