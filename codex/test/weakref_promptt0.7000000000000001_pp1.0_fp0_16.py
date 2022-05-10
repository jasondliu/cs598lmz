import weakref
# Test weakref.ref
#
# The first reference to an object must be strong, so we store a strong reference
# in a list.
#
# Note that this test is deliberately not wrapped in a test case class.

class C(object):
    pass

def f():
    pass

