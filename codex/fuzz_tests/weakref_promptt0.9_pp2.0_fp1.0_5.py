import weakref
# Test weakref.ref(obj)
#
# This is a nose test generator.

from weakref import ref
from types import MethodType

from nose import SkipTest
from nose.tools import *
from nose.tools import nottest
from nose.tools import raises

def wr_refs_equal(r1, r2):
    return (
        (r1 is None and r2 is None) or (
        isinstance(r1, ref) and isinstance(r2, ref) and
        r1() is r2() and r1.__eq__ is r2.__eq__ and
        r1.__hash__ is r2.__hash__)
    )

class Base(object):
    pass

class TestModuleFunctions(object):

    def check_ref(self, obj, check_methods=True):
        r = ref(obj)
        same_obj = r()
        assert obj is same_obj, "Ref and original must be same objects"
        # Make sure the object hasn't been collected
        weakref.dereference(r)
        obj_id = id
