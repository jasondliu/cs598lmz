import weakref
# Test weakref.ref()

class C:
    pass

c = C()
r = weakref.ref(c)
if r() is not c:
    print("Error: weakref.ref()")

# Test weakref.proxy()

c = C()
p = weakref.proxy(c)
if p is not c:
    print("Error: weakref.proxy()")

# Test weakref.getweakrefcount()

c = C()
r = weakref.ref(c)
if weakref.getweakrefcount(c) != 1:
    print("Error: weakref.getweakrefcount()")

# Test weakref.getweakrefs()

c = C()
r = weakref.ref(c)
wr = weakref.getweakrefs(c)
if len(wr) != 1 or wr[0] is not r:
    print("Error: weakref.getweakrefs()")

# Test weakref.WeakKeyDictionary

class Key:
    pass

d = weakref.WeakKeyDictionary()
k1 =
