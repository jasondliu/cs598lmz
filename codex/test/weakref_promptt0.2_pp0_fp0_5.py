import weakref
# Test weakref.ref()

class C:
    pass

c = C()
r = weakref.ref(c)
print(r)
print(r())

del c
print(r())

# Test weakref.proxy()

class C:
    pass

c = C()
p = weakref.proxy(c)
print(p)
print(p.__class__)

del c
print(p)

# Test weakref.getweakrefcount()

class C:
    pass

c = C()
r = weakref.ref(c)
print(weakref.getweakrefcount(c))

# Test weakref.getweakrefs()

class C:
    pass

c = C()
r = weakref.ref(c)
print(weakref.getweakrefs(c))

# Test weakref.finalize()

class C:
    pass

c = C()
r = weakref.finalize(c, lambda x: print("finalized"))
print(r)

del c
print(r)
