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

o2 = p
print(o2)

o.attr = 42
print(p.attr)

try:
    p.attr2
except AttributeError:
    print("AttributeError")

try:
    p.foo = 12
except TypeError:
    print("TypeError")

try:
    del p.attr
except TypeError:
    print("TypeError")

try:
    del p.attr
