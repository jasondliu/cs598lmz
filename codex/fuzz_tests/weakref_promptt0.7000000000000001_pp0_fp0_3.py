import weakref
# Test weakref.ref
class A: pass
a = A()
b = weakref.ref(a)
assert b() == a
del a
assert b() is None

# Test weakref.proxy
a = A()
b = weakref.proxy(a)
assert b.__class__.__name__ == "weakproxy"
assert b == a
del a
try:
    b.foo
except ReferenceError:
    pass
else:
    assert False

# Test weakref.getweakrefcount
a = A()
b = weakref.ref(a)
assert weakref.getweakrefcount(a) == 1
assert weakref.getweakrefcount(b) == 0

# Test weakref.getweakrefs
a = A()
b = weakref.ref(a)
assert weakref.getweakrefs(a) == [b]
assert weakref.getweakrefs(b) == []

# Test weakref.WeakKeyDictionary
class MyClass:
    pass

a = MyClass()
b = MyClass()
d = weakref.WeakKey
