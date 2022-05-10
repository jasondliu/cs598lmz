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

del o
print(r())

del o2
print(r())

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)

print(p)

o2 = p
print(o2)

del o
#print(p)

del o2
#print(p)

# Test weakref.getweakrefcount() and weakref.getweakrefs()

a = C()
d = weakref.WeakValueDictionary()
d[1] = a
d[2] = a
print(weakref.getweakrefcount(a))
print(weakref.getweakrefs(a))

# Test weakref.finalize()

a = C()

def callback(wr, a=a):
    print(wr)
    print(a)

wr = weakref
