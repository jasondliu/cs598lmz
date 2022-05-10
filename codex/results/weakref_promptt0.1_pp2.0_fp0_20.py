import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)

print(r)
print(r())

o2 = r()
print(o2)

del o
print(r())

del o2
print(r())

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)

print(p)

o2 = p
print(o2)

del o
try:
    print(p)
except ReferenceError:
    print("ReferenceError")

del o2
try:
    print(p)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()

o = C()
print(weakref.getweakrefcount(o))

r = weakref.ref(o)
print(weakref.getweakrefcount(o))

p = weakref.proxy(o)
print(weakref.getweakrefcount(o))

del r
print(weakref.getweakrefcount
