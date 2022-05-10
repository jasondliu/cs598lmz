import weakref
# Test weakref.ref() and weakref.proxy() with a class and an instance.
import weakref
import gc

class C:
    pass

o = C()
r = weakref.ref(o)
p = weakref.proxy(o)

print(r(), p)

o2 = r()

print(o2 is o)

o3 = p

print(o3 is o)

print(r() is o is o2 is o3)

o = None

print(r() is None)

try:
    print(p)
except ReferenceError:
    print("ReferenceError")

gc.collect()

print(r() is None)

try:
    print(p)
except ReferenceError:
    print("ReferenceError")

# Test weakref.ref() and weakref.proxy() with a dict.
import weakref
import gc

d = {}
r = weakref.ref(d)
p = weakref.proxy(d)

print(r(), p)

d2 = r()

print(d
