import weakref
# Test weakref.ref() on a plain old class.
class C:
    pass


obj = C()
r = weakref.ref(obj)
