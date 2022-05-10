import weakref
# Test weakref.ref()

class C:
    pass

obj = C()
r = weakref.ref(obj)
