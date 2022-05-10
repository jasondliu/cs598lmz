import weakref
# Test weakref.ref()
class C:
    pass
o = C()
r = weakref.ref(o)
print(r)
print(r())

# Test weakref.proxy()
o2 = C()
p = weakref.proxy(o2)
print(p)

# Test weakref.getweakrefcount()
a = C()
b = C()
c = C()
w1 = weakref.ref(a)
w2 = weakref.ref(b)
w3 = weakref.ref(c)
print(weakref.getweakrefcount(a))

# Test weakref.getweakrefs()
print(weakref.getweakrefs(a))

# Test weakref.finalize()
a = C()
weakref.finalize(a, print, 'finalized!')
del a

# Test weakref.WeakKeyDictionary
d = weakref.WeakKeyDictionary()
o = C()
d[o] = 1
print(d[o])
del o
print(d)

# Test weakref.WeakValueD
