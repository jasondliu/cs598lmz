import weakref
# Test weakref.ref

# Fredrik Lundh's weakref.ref example
class C:
    pass

o = C()
r = weakref.ref(o)
