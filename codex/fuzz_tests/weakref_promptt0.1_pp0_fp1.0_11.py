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

o4 = r2()
print(o4)

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)

print(p)

o2 = p
print(o2)

o3 = C()
p2 = weakref.proxy(o3)
print(p2)

o4 = p2
print(o4)

# Test weakref.getweakrefcount()

o = C()

print(weakref.getweakrefcount(o))

r = weakref.ref(o)

print(weakref.getweakrefcount(o))

p = weakref.proxy(o)

print(weakref.getweakrefcount(
