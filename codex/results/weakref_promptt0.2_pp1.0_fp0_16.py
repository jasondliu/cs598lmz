import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)
print(r() is None)

o2 = C()
r2 = weakref.ref(o2)
print(r2)
print(r2() is o2)
print(r2() is None)

o = None
print(r() is None)

o2 = None
print(r2() is None)

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
print(p)
print(p is o)
print(p.__class__ is C)

o2 = C()
p2 = weakref.proxy(o2)
print(p2)
print(p2 is o2)
print(p2.__class__ is C)

o = None
try:
    print(p)
except ReferenceError:
    print("ReferenceError")

o2 = None
try:
    print
