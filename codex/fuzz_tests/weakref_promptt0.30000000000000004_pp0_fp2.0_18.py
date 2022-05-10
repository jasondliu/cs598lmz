import weakref
# Test weakref.ref()

class C:
    pass

c = C()
r = weakref.ref(c)
print(r)
print(r())
print(r() is c)

del c
print(r())

print(r() is None)

# Test weakref.proxy()

c = C()
p = weakref.proxy(c)
print(p)
print(p is c)

del c
try:
    print(p)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()

c = C()
print(weakref.getweakrefcount(c))

r = weakref.ref(c)
print(weakref.getweakrefcount(c))

p = weakref.proxy(c)
print(weakref.getweakrefcount(c))

del r
print(weakref.getweakrefcount(c))

del p
print(weakref.getweakrefcount(c))

# Test weakref.getweakrefs()

c = C()

