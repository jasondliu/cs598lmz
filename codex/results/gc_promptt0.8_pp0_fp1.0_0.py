import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
import sys
s = 'abc'
s = None
print(gc.collect())
print(gc.collect())
print(gc.collect())
print(gc.get_count())
print(gc.garbage)

# Test weakref
import weakref
x = weakref.WeakValueDictionary()

def finalize(reference):
    print('called finalizer')

o = object()
x[o] = 1
o_id = id(o)
print(x)
del o
print(gc.collect())
wr = weakref.ref(o, finalize)
print(gc.collect())

# Test weakref.getweakrefcount
import weakref
class Foo: pass
f = Foo()
w = weakref.ref(f)
print(weakref.getweakrefcount(f))
del f
print(weakref.getweakrefcount(w))

#Test weakref.getweakrefs
import weakref
class Foo: pass
f = Foo()
w = weakref.ref(f)
print(weakref.getweakrefs
