import weakref
# Test weakref.ref() with a class that has a __del__ method.
#
# When a class has a __del__ method, its instances are not directly
# collectible.  A reference to an instance is collectible only when the
# __del__ method has been executed.  This was not always the case.
#
# The tests here were written to exercise the implementation of
# PyWeakref_NewRef() in Objects/weakrefobject.c.  That implementation
# has since been modified and some of the tests are no longer relevant.

class C:

    def __del__(self):
        pass

class D:
    pass

class E(C):
    pass

class F(D, C):
    pass

class G(D, C):

    def __del__(self):
        pass

class H(D, C):

    def __del__(self):
        pass

def test(cls):
    o = cls()
    o_id = id(o)
    o_ref = weakref.ref(o)
