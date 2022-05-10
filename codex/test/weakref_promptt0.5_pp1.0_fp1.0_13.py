import weakref
# Test weakref.ref() on a finalizing object.

class C:
    pass

def ref(obj):
    return weakref.ref(obj)

