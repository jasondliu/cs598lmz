import weakref
# Test weakref.ref(x)
class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

del o
print(r())

# Test weakref.getweakrefcount(x)
a = C()
b = C()

w1 = weakref.ref(a)
w2 = weakref.ref(a)
w3 = weakref.ref(b)

print(weakref.getweakrefcount(a))
print(weakref.getweakrefcount(b))
print(weakref.getweakrefcount(C))

# Test weakref.getweakrefs(x)
print(weakref.getweakrefs(a))
print(weakref.getweakrefs(b))
print(weakref.getweakrefs(C))

# Test weakref.proxy(x[, callback])
class D:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<D instance '%s'>" % self
