import ctypes
# Test ctypes.CFUNCTYPE with both a few basic types, and various kinds of
# derived classes.
class TypeTestCase(object):

    def test_CFUNCTYPE_int_void(self):
        self.assertIsInstance(CFUNCTYPE(c_int, None), type(CFUNCTYPE))
        self.assertEqual(CFUNCTYPE(c_int, None).argtypes, ())
        self.assertEqual(CFUNCTYPE(c_int, None).restype, c_int)
        self.assertEqual(CFUNCTYPE(c_int, None).__name__, '<unknown>')
        self.assertEqual(str(CFUNCTYPE(c_int, None)), '<unknown>() -> c_int')

    def test_CFUNCTYPE_int_int(self):
        self.assertIsInstance(CFUNCTYPE(c_int, (c_int,)), type(CFUNCTYPE))
        self.assertEqual(CFUNCTYPE(c_int, (c_int,)).arg
