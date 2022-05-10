import weakref
# Test weakref.ref(simple_class),
# but catch the Func() expansion warning given by Python 2.4 w/o -3
# and fix it to Python 2.4 style.
from warnings import warnpy3k

import func_signature
from func_signature import signature
from func_signature import Class as Func
from vatest import TestF

class TestCls:
    def test(self):
        obj = fnc()
        assert thunk(obj) == [1, 2]
        assert id(obj) == unthunk(obj)
        r = weakref.ref(obj)
        assert r() is obj
        del obj
        assert r() is None

# Test function with a docstring
fnc2.__doc__ = """
foo: bar
baz: blah blah blah blah blah blah blah blah blah blah blah blah blah
blah blah blah blah blah
"""

class TestF:
    def test(self):
        sig = signature(fnc)
        sig2 = signature(fnc2)
