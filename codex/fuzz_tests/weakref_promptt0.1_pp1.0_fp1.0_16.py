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

print(r is r2)
print(o is o2)
print(o3 is o4)

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)

print(p)

o.attr = 'foo'
print(p.attr)

o2 = C()
p2 = weakref.proxy(o2)
print(p2)

o2.attr = 'bar'
print(p2.attr)

print(p is p2)
print(o is o2)

# Test weakref.getweakrefcount()

o = C()
print(weakref.getweakrefcount
