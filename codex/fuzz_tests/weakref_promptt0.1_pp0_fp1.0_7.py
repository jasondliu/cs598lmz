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

del o2
print(r2())

print(r())

del o
print(r())

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
print(p)

o2 = C()
p2 = weakref.proxy(o2)
print(p2)

del o2
try:
    print(p2)
except ReferenceError:
    print("ReferenceError")

print(p)

del o
try:
    print(p)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()

o = C()
print(weakref.getweakrefcount(o))

r = weakref.ref(o)
print(weakref.getweak
