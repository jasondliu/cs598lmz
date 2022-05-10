import weakref
# Test weakref.ref()

class C:
    pass

c = C()
r = weakref.ref(c)
print(r)

r() is c

# Test weakref.proxy()

p = weakref.proxy(c)
print(p)
p is c

del c
print(r())

# Test weakref.getweakrefcount() and weakref.getweakrefs()

a = C()
b = C()
c = C()
d = C()
p = weakref.proxy(c)
r = weakref.ref(d)

weakref.getweakrefcount(a)
weakref.getweakrefs(a)

weakref.getweakrefcount(b)
weakref.getweakrefs(b)

weakref.getweakrefcount(c)
weakref.getweakrefs(c)

weakref.getweakrefcount(d)
weakref.getweakrefs(d)

# Test weakref.WeakKeyDictionary

d = weakref.WeakKeyDictionary()
d['regular
