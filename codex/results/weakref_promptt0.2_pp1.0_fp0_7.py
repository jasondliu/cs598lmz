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

o3 = C()
r2 = weakref.ref(o3)
print(r2)
print(r2())

o = None
print(r())

o3 = None
print(r2())

# Test weakref.proxy()

class C:
    pass

o = C()
p = weakref.proxy(o)

print(p)

o.foo = 1
print(p.foo)

o2 = C()
p2 = weakref.proxy(o2)
print(p2)

o = None
try:
    print(p.foo)
except ReferenceError:
    print("ReferenceError")

o2 = None
try:
    print(p2.foo)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()

class C:
