import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2)
print(r2)
print(r2())

o = o2 = None
print(r())
print(r2())

# Test weakref.proxy()

class C:
    pass

o = C()
p = weakref.proxy(o)
print(p)

o2 = C()
p2 = weakref.proxy(o2)
print(p2)

o = o2 = None
try:
    print(p)
except ReferenceError:
    print("ReferenceError")

try:
    print(p2)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()

class C:
    pass

o = C()
print(weakref.getweakrefcount(o))

r = weakref.ref(o)
