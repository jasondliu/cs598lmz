import weakref
# Test weakref.ref.
import weakref

class C: pass

o = C()
r = weakref.ref(o)

print(r())

o2 = r()
print(o2 is o)

o2 = C()
print(r() is None)

o = C()
r = weakref.ref(o)
print(r() is o)

o2 = C()
o2 = o
print(r() is o)

o2 = C()
print(r() is None)

# Test weakref.proxy.
import weakref

class C: pass

o = C()
p = weakref.proxy(o)

print(p.__class__.__name__)

print(p is o)

o2 = C()
o2 = o
print(p is o)

o2 = C()
print(p is None)

# Test weakref.getweakrefcount.
import weakref

class C: pass

o = C()
r = weakref.ref(o)

print(weak
