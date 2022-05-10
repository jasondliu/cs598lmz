import weakref
# Test weakref.ref
class C:
    pass
o = C()
r = weakref.ref(o)
print(r)
print(r())
del o
print(r)
print(r())

# Test weakref.proxy
o = C()
p = weakref.proxy(o)
print(p)
print(p.x)
#del o
#print(p)
#print(p.x)

# Test weakref.WeakKeyDictionary
d = weakref.WeakKeyDictionary()
o = C()
d[o] = 1
print(d[o])
del o
print(d)

# Test weakref.WeakValueDictionary
d = weakref.WeakValueDictionary()
o = C()
d[1] = o
print(d[1])
del o
print(d)
