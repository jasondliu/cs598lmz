import weakref
# Test weakref.ref(g) is g

# This is a test for the weakref module.
# This test makes sure that weakref.ref(g) is g

import weakref

class C:
    pass

def callback(r):
    print("callback called")

def test_ref():
    o = C()
    r = weakref.ref(o, callback)
    assert r is o
    del o
    print("end of test")

test_ref()
