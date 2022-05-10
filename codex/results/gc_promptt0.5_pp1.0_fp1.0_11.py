import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()

class A:
    def __init__(self, value=42):
        self.value = value
    def __repr__(self):
        return 'A(%s)' % self.value
    def __del__(self):
        print 'A.__del__'

# Test weakref.ref
a = A()
r = weakref.ref(a)
print r
print r()
del a
print gc.collect()
print r()
del r
print gc.collect()

# Test weakref.proxy
a = A()
p = weakref.proxy(a)
print p
print p.value
del a
print gc.collect()
print p.value
del p
print gc.collect()

# Test weakref.getweakrefcount
print weakref.getweakrefcount(A)
print weakref.getweakrefcount(A())

# Test weakref.getweakrefs
print weakref.getweakrefs(A)
print weakref.getweakrefs(A())


