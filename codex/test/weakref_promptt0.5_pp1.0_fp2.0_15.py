import weakref
# Test weakref.ref
class C:
    pass
c = C()
r = weakref.ref(c)
