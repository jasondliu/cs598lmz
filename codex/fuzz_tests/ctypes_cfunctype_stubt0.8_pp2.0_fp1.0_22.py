import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    pass

class C(object):
    __slots__ = "a"
    def meth(self):
        pass
    @staticmethod
    def othermeth():
        pass

def f(*args):
    return 2
f.a = 3

def g(**kwds):
    return 2
g.a = 3

import sys
if sys.version_info[:2] >= (2,6):
    class C(object):
        __slots__ = "b", "c"
        @staticmethod
        def sm():
            pass
        @classmethod
        def cm(self):
            pass

import _ctypes_test

class EX(Exception):
    pass

class TestFrom_param(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(ctypes.from_param(None), None)
        self.assertEqual(ctypes.from_param(1), 1)
        self.assertEqual(ctypes.from_param(1L), 1)
        self.assertE
