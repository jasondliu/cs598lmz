import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)

print(r())

o2 = r()
print(o2 is o)

o3 = C()
r2 = weakref.ref(o3)
print(r2() is o3)

print(r() is o)

o = None
print(r() is None)
print(r2() is None)

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)

print(p.__class__)

o.x = 1
print(p.x)

o2 = C()
p2 = weakref.proxy(o2)

print(p2.__class__)

o2.x = 1
print(p2.x)

o = o2 = None

try:
    p.x
except ReferenceError:
    print("ReferenceError")

try:
    p2.x
except ReferenceError:
    print("ReferenceError")

#
