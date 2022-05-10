import weakref
# Test weakref.ref
class Foo:
    def __init__(self, name):
        self.name = name

f = Foo("Dave")
r = weakref.ref(f)
assert r().name == "Dave"
f = None
assert r() is None

# Test weakref.proxy
class Foo:
    def __init__(self, name):
        self.name = name

f = Foo("Dave")
r = weakref.proxy(f)
assert r.name == "Dave"
f = None
try:
    r.name
except ReferenceError:
    pass
else:
    print("expected ReferenceError")

# Test weakref.getweakrefcount
class Foo:
    pass

f = Foo()
r = weakref.ref(f)
assert weakref.getweakrefcount(f) == 1

# Test weakref.getweakrefs
class Foo:
    pass

f = Foo()
r = weakref.ref(f)
assert weakref.getweakrefs(f) == [r]

# Test weakref.finalize

