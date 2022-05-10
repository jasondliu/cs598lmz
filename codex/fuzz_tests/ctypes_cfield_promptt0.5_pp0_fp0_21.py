import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test_CField(self):
        # Create a CField with a function type.
        f = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
        self.assertEqual(f.__name__, 'CFUNCTYPE')
        self.assertEqual(f.__module__, 'ctypes')
        self.assertEqual(f.__doc__, 'Create a C callable function prototype instance.')
        self.assertEqual(f.__dict__, {})
        self.assertEqual(f.__args__, (ctypes.c_int, ctypes.c_int))
        self.assertEqual(f.__restype__, ctypes.c_int)
        # Create a CField with a C structure type.
        class S(ctypes.Structure):
            _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]
        s = ctypes.CField(S)
