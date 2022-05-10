import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)

o2 = C()
r2 = weakref.ref(o2)
print(r2)
print(r2())
print(r2() is o2)

print(r is r2)
print(r() is r2())

o = None
print(r())
print(r2())

print(r() is r2())

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
print(p)
print(p is o)
print(p.__class__)

o2 = C()
p2 = weakref.proxy(o2)
print(p2)
print(p2 is o2)
print(p2.__class__)

print(p is p2)
print(p is o2)
print(p2 is o)

o = None
try:
    print(
