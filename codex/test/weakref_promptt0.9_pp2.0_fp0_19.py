import weakref
# Test weakref.ref
class C(object):
    pass

wr = weakref.ref(C)
