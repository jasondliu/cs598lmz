import weakref
# Test weakref.ref()
def ref(arg):
    return weakref.ref(arg)

class C:
    pass

o = C()
r = ref(o)
assert r() is o
del o
assert r() is None
# Test weakref.proxy()
def proxy(arg):
    return weakref.proxy(arg)

class C:
    pass

o = C()
p = proxy(o)
assert p is o
del o
try:
    p
except ReferenceError:
    pass
else:
    assert False, "ReferenceError not raised"
# Test weakref.getweakrefcount()
def getweakrefcount(arg):
    return weakref.getweakrefcount(arg)

class C:
    pass

o = C()
r = ref(o)
assert getweakrefcount(o) == 1
del r
assert getweakrefcount(o) == 0
# Test weakref.getweakrefs()
def getweakrefs(arg):
    return weakref.getweakrefs(arg)

class C:
    pass

