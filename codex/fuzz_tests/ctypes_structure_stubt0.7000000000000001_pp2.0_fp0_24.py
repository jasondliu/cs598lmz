import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    y = ctypes.c_int()


_testcapi = test_support.import_module('_testcapi')

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.s = S()
        self.s.x = 42
        self.s.y = -1
        self._testcapi.test_struct_fields(self.s)
        self.assertEqual(self.s.x, 42)
        self.assertEqual(self.s.y, -1)

class TestCase(BaseTestCase):
    def test_direct_access(self):
        self.s.x = 1729
        self.s.y = 42
        self._testcapi.test_struct_fields(self.s)
        self.assertEqual(self.s.x, 1729)
        self.assertEqual(self.s.y, 42)

        self.s.x = 0
        self.s.y = 0
        self._testcapi.
