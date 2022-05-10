import weakref
# Test weakref.ref()

class C:
    pass

o = C()
r = weakref.ref(o)
assert r() is o

try:
    weakref.ref(1)
except TypeError:
    pass
else:
    print("Failed to raise TypeError")

# Test weakref.proxy()

o = C()
p = weakref.proxy(o)
assert p is o

try:
    weakref.proxy(1)
except TypeError:
    pass
else:
    print("Failed to raise TypeError")

# Test weakref.getweakrefcount()

o = C()
assert weakref.getweakrefcount(o) == 0
r = weakref.ref(o)
assert weakref.getweakrefcount(o) == 1

try:
    weakref.getweakrefcount(1)
except TypeError:
    pass
else:
    print("Failed to raise TypeError")

# Test weakref.getweakrefs()

o = C()
assert weakref.getweakrefs(o)
