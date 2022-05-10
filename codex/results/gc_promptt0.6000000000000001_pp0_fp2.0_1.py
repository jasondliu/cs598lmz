import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
class A:
    pass
a = A()
b = A()
print(gc.collect())
print(gc.collect())
print(gc.collect())
print('finalizing', gc.collect())

print('garbage:', gc.garbage)

# Test object.__del__()
class A:
    def __del__(self):
        print('A.__del__')

a = A()
print('before')
del a
print('after')

# Test weakref.getweakrefcount()
class A:
    pass
a = A()
print(weakref.getweakrefcount(a))
b = weakref.ref(a)
print(weakref.getweakrefcount(a))
c = weakref.ref(a)
print(weakref.getweakrefcount(a))
del b
print(weakref.getweakrefcount(a))
del c
print(weakref.getweakrefcount(a))

# Test weakref.getweakrefs()
class A:
    pass
a = A()
