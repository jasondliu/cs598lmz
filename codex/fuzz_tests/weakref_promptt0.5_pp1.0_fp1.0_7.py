import weakref
# Test weakref.ref()
#
# This test is NOT run on PyPy because the weakref module is not
# implemented there yet.
#
# This test is also not run on Android because the weakref module is
# not implemented there yet.

import gc
import sys

class Foo(object):
    pass

def test_weakref_ref():
    # Create a reference to a Foo object
    foo = Foo()
    foo_ref = weakref.ref(foo)
    assert foo_ref() is foo
    # Delete the original Foo object, and make sure the reference still works
    del foo
    gc.collect()
    assert foo_ref() is not None
    # Delete the reference, and make sure it's really gone
    del foo_ref
    gc.collect()
    assert foo_ref() is None

def test_weakref_ref_callable():
    # Create a reference to a Foo object
    foo = Foo()
    foo_ref = weakref.ref(foo)
    assert foo_ref() is foo
    # Delete the original Foo object, and make sure the reference
