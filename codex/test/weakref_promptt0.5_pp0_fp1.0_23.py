import weakref
# Test weakref.ref(func)
def f():
    pass
assert type(weakref.ref(f)) is weakref.ReferenceType
assert weakref.ref(f)() is f

# Test weakref.proxy(func)
def f():
    pass
p = weakref.proxy(f)
assert type(p) is weakref.CallableProxyType
assert p() is f

# Test weakref.getweakrefcount(func)
def f():
    pass
assert weakref.getweakrefcount(f) == 0

# Test weakref.getweakrefs(func)
def f():
    pass
assert weakref.getweakrefs(f) == []
