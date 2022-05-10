import weakref
# Test weakref.ref and callback to avoid reference cycles.
# This test is not specific to OrderedDict, but we have no other way to test
# forced finalization at the moment.

import pickle

class Dummy(object):
    pass

# Test reference counters.
def test_ref(c, x):
    ref = weakref.ref(x, c)
    assert ref() is x

def test_ref_repr(c, x):
    ref = weakref.ref(x, c)
    repr(ref)

# Test callbacks.
class A:
    pass

def test_callback(c, x):
    ref = weakref.ref(x, c)
    assert ref() is x

def test_callback_with_args(c, x, arg):
    ref = weakref.ref(x, c, arg)
    assert ref() is x
    assert test_callback_with_args.arg is arg

