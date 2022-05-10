import weakref
# Test weakref.ref()

class C:
    pass

c = C()
r = weakref.ref(c)
print(r)
print(r())

c = None
print(r())

# Test weakref.proxy()

c = C()
p = weakref.proxy(c)
print(p)

c = None
try:
    print(p)
except ReferenceError:
    print("ReferenceError")

# Test weakref.getweakrefcount()

c = C()
r1 = weakref.ref(c)
r2 = weakref.ref(c)
print(weakref.getweakrefcount(c))

# Test weakref.getweakrefs()

c = C()
r1 = weakref.ref(c)
r2 = weakref.ref(c)
print(weakref.getweakrefs(c))

# Test weakref.WeakKeyDictionary

d = weakref.WeakKeyDictionary()
c1 = C()
c2 = C()
d[c1] = 1
d[c2
