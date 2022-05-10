import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
print(r)
print(r())

o2 = C()
r2 = weakref.ref(o2, lambda x: print('dead'))

del o2
print('done')

# Test weakref.proxy()

class C:
    def __init__(self, name):
        self.name = name

o = C('bob')
p = weakref.proxy(o)
print(p.name)

o.name = 'sue'
print(p.name)

del o
try:
    print(p.name)
except ReferenceError:
    print('dead')

# Test weakref.getweakrefcount()

class C:
    pass

o = C()
print(weakref.getweakrefcount(o))

r = weakref.ref(o)
print(weakref.getweakrefcount(o))

r2 = weakref.ref(o)
