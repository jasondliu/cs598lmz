import weakref
# Test weakref.ref.
class C:
    pass

obj = C()
r = weakref.ref(obj)

# Test weakref.proxy
p = weakref.proxy(obj)
p.foo = 12

assert r().foo == 12
assert obj.foo == 12

# Test weakref.getweakrefs
wr = weakref.getweakrefs(obj)
assert len(wr) == 1
assert wr[0]() is obj

# Test weakref.getweakrefcount
assert weakref.getweakrefcount(obj) == 1

# Test weakref.WeakMethod
class C:
    def foo(self):
        pass

meth = C().foo
r = weakref.WeakMethod(meth)
assert r() is meth

# Test weakref.WeakKeyDictionary
dct = weakref.WeakKeyDictionary()
dct[obj] = 12
assert dict(dct) == {obj: 12}

del obj
assert dict(dct) == {}

# Test weakref.WeakValueDictionary
dct = weakref.WeakValue
