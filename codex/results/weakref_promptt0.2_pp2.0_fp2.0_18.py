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
print(weakref.getweakrefcount(o))

# Test weakref.getweakrefs()
print(weakref.getweakrefs(o))

# Test weakref.finalize()
def callback(r):
    print('callback({!r})'.format(r))

o3 = C()
f = weakref.finalize(o3, callback, o3)
print(f.alive)
del o3
print(f.alive)

# Test weakref.WeakKeyDictionary
class Cheese:
    def __init__(self, kind):
        self.kind = kind
    def __repr__(self):
        return 'Cheese(%r)' % self.kind

stock = weakref.WeakKeyD
