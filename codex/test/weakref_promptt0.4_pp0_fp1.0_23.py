import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())
print(r() is o)

# Test weakref.getweakrefcount()

a = C()
b = C()
r1 = weakref.ref(a)
r2 = weakref.ref(a)
r3 = weakref.ref(b)
print(weakref.getweakrefcount(a))
print(weakref.getweakrefcount(b))

# Test weakref.getweakrefs()

print(weakref.getweakrefs(a))
print(weakref.getweakrefs(b))

# Test weakref.proxy()

p = weakref.proxy(a)
print(p)
print(p is a)

# Test weakref.finalize()

class Finalize:
    def __init__(self, arg):
        self.arg = arg
    def __del__(self):
        print('Finalized', self.arg)

f = Final
