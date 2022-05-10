import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Test(unittest.TestCase):
    def test_basic(self):
        # Test that ctypes.c_int.__doc__ is correct
        self.assertEqual(ctypes.c_int.__doc__, "ctypes.c_int(value, /)")

    def test_gc(self):
        class X(object):
            _refs_ = []
        from _testcapi import get_exception
        get_exception(X)   # don't complain about missing ref

    def test_fields(self):
        # Make sure that c_char_p._fields_ is a tuple containing one item
        # as documented.
        self.assertEqual(type(ctypes.c_char_p._fields_), tuple)
        self.assertEqual(len(ctypes.c_char_p._fields_), 1)

    def test_fields_is_immutable(self):
        # Make sure that _fields_ is immutable
        self.assertRaises(TypeError, setattr, ctypes.c_char_p,

