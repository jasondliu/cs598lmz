import weakref
# Test weakref.ref
class C:
    pass
o = C()
r = weakref.ref(o)
r() is o

r() is None

del o
r() is None

# Test weakref.proxy
o = C()
p = weakref.proxy(o)
p is o

p.foo = 1
o.foo

del o
try:
    p.foo
except ReferenceError:
    pass
else:
    print('Expected ReferenceError')

# Test weakref.getweakrefcount
a = C()
b = C()
weakref.getweakrefcount(a)

weakref.getweakrefcount(b)

r = weakref.ref(a)
weakref.getweakrefcount(a)

del r
weakref.getweakrefcount(a)

# Test weakref.getweakrefs
a = C()
b = C()
r = weakref.ref(a)
s = weakref.ref(a)
weakref.getweakrefs(a) == [r, s]

weakref
