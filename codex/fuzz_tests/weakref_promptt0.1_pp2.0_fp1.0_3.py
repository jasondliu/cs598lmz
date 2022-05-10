import weakref
# Test weakref.ref(x)

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

del o
print(r())

# Test weakref.ref(x, callback)

class C:
    pass

o = C()
l = []
def callback(arg):
    l.append(arg)

r = weakref.ref(o, callback)
print(r)
print(r())

del o
print(r())
print(l)

# Test weakref.proxy(x)

class C:
    pass

o = C()
p = weakref.proxy(o)
print(p)
print(p.__class__)

del o
try:
    print(p)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount(x)

class C:
    pass

o = C()
print(weakref.getweakrefcount(o))

r = weakref.ref(o)

