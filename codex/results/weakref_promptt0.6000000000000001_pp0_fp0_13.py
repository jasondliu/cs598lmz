import weakref
# Test weakref.ref() with a cycle.
class C:
    pass
a = C()
a.x = a
w = weakref.ref(a)
del a
try:
    w().x
except ReferenceError:
    print('ReferenceError')
