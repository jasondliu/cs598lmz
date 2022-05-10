import weakref
# Test weakref.ref(some_object).
#
# This is a fairly minimal test of weakref.  The test is not complete,
# but it should be enough to demonstrate that weakref.ref works.
# (It is not possible to test the behavior of weakref on cyclic structures
# without a lot more code.)

import weakref
import gc

_debug = 0

#
# For the purpose of the test, we define a custom class that uses weakrefs.
#

class MyClass:
    def __init__(self, name):
        self.name = name
        self._wrefs = {}

    def __repr__(self):
        return "<MyClass %s>" % self.name

