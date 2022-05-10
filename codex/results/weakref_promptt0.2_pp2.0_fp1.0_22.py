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
print(r)
print(r())

o4 = C()
r3 = weakref.ref(o4, lambda x: print('dead'))
print(r3)
print(r3())

o4 = None
print(r3)
print(r3())

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
print(p)

o.attr = 42
print(p.attr)

o2 = C()
p2 = weakref.proxy(o2)
print(p2)

o2 = None
try:
    print(p2.attr)
except ReferenceError:
    print('ReferenceError')

# Test
