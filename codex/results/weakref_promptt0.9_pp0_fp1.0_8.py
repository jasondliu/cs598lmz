import weakref
# Test weakref.ref is working.
a = weakref.ref(long())

assertNull(a)

b = weakref.ref(long(2))

assertNotNull(b)

print weakref.getweakrefcount(1)
print weakref.getweakrefs(1)
