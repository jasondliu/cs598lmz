import weakref
# Test weakref.ref

# Fredrik Lundh's weakref.ref example
class C:
    pass

o = C()
r = weakref.ref(o)
print r
del o
print r()

# Test that weakref.ref fails when it should

try:
    weakref.ref(1)
except TypeError:
    pass
else:
    print "weakref.ref succeeded with int"

try:
    weakref.ref([])
except TypeError:
    pass
else:
    print "weakref.ref succeeded with list"

try:
    weakref.ref(())
except TypeError:
    pass
else:
    print "weakref.ref succeeded with tuple"

try:
    weakref.ref(1.0)
except TypeError:
    pass
else:
    print "weakref.ref succeeded with float"

# Test that weakref.ref accepts objects with the PY_WRITE_RESTRICTED flag

def g():
    x = C()
    x.__dict__.setdefault('__wr', []).append
