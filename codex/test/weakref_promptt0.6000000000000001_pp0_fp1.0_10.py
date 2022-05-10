import weakref
# Test weakref.ref()
class C:
    pass
o = C()
r = weakref.ref(o)
w = weakref.ref(o)
o.x = 1
print(r())
print(w())
del o
print(r())
print(w())

# Test weakref.proxy()
o = C()
p = weakref.proxy(o)
w = weakref.proxy(o)
o.x = 1
print(p.x)
print(w.x)
del o
try:
    print(p.x)
except ReferenceError:
    print("ReferenceError")
try:
    print(w.x)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()
o = C()
print(weakref.getweakrefcount(o))
a = weakref.ref(o)
print(weakref.getweakrefcount(o))
del a
print(weakref.getweakrefcount(o))

# Test weakref.getweakrefs()
o = C()
l = weak
