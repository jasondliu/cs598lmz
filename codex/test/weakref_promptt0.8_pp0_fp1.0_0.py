import weakref
# Test weakref.ref
class C:
    pass
a = C()
b = weakref.ref(a)
