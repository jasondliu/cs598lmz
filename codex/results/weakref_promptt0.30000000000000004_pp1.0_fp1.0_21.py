import weakref
# Test weakref.ref()
import gc

class A:
    pass

a = A()
r = weakref.ref(a)
print(r())
del a
gc.collect()
print(r())

# Test weakref.WeakKeyDictionary()
class A:
    pass

a = A()
d = weakref.WeakKeyDictionary()
d[a] = 1
print(d[a])
del a
print(d)

# Test weakref.WeakValueDictionary()
class A:
    pass

a = A()
d = weakref.WeakValueDictionary()
d[1] = a
print(d[1])
del a
print(d)

# Test weakref.finalize()
class A:
    pass

a = A()
f = weakref.finalize(a, lambda x: print('finalized', x))
print(f.alive)
del a
print(f.alive)
gc.collect()
print(f.alive)

# Test weakref.WeakSet()
class A:
   
