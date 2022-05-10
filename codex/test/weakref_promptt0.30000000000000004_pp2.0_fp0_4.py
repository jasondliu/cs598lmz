import weakref
# Test weakref.ref() and weakref.proxy()

class C:
    pass

o = C()
r = weakref.ref(o)
p = weakref.proxy(o)

print(r)
print(p)
print(r())
print(p)

del o
print(r)
print(p)

try:
    print(r())
except ReferenceError:
    print("ReferenceError")

try:
    print(p)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()

class C:
    pass

o = C()
a = weakref.ref(o)
b = weakref.ref(o)
c = weakref.ref(o)
d = weakref.ref(o)

print(weakref.getweakrefcount(o))
print(weakref.getweakrefcount(a))
print(weakref.getweakrefcount(b))
print(weakref.getweakrefcount(c))
print(weakref.getweakrefcount(d))

