import weakref
# Test weakref.ref() with objects of the same type.
# This test checks the following:
#
#  -- weakref objects can be created in various ways.
#  -- weakref objects are callable, returning the referenced object or None.
#  -- weakref objects are reusable, but only once.
#  -- weakref objects can be hashed and compared to other weakref objects.
#  -- weakref objects can be used as dictionary keys.
#  -- weakref objects compare unequal to objects of different types.

class C(object):
    pass

def test_new(C_class):
    c = C_class()
    c_ref = weakref.ref(c)
    assert c_ref() is c


def test_proxy(C_class):
    c = C_class()
    c_ref = weakref.proxy(c)
    assert c_ref is c


def test_ref_call(C_class):
    c = C_class()
    c_ref = weakref.ref(c)
    assert c_ref is not c and c_ref() is c



