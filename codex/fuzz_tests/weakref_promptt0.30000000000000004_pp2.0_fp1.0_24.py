import weakref
# Test weakref.ref(x)
assert weakref.ref(x)() == x
# Test weakref.ref(x, callback)
def callback(obj):
    global x
    x = None
    assert obj is None
x = 1
assert weakref.ref(x, callback)() == 1
del x
assert x is None
# Test weakref.proxy(x)
assert weakref.proxy(x) is None
x = 1
assert weakref.proxy(x) == 1
del x
assert x is None
# Test weakref.getweakrefcount(x)
assert weakref.getweakrefcount(x) == 0
x = 1
assert weakref.getweakrefcount(x) == 0
x = weakref.ref(x)
assert weakref.getweakrefcount(x) == 1
x = weakref.proxy(x)
assert weakref.getweakrefcount(x) == 2
x = weakref.ref(x)
assert weakref.getweakrefcount(x) == 3
del x
assert x is None
# Test weakref.getweakrefs(x
