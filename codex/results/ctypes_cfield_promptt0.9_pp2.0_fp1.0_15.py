import ctypes
# Test ctypes.CField
class TestCField(unittest.TestCase):
    def test___repr__(self):
        try:
            self.assertEqual(repr(ctypes.CField()), "<CField '_fields_'>")
        except (TypeError, NotImplementedError):
            self.fail("repr(ctypes.CField) raised TypeError or NotImplementedError")

    def test___eq__(self):
        try:
            self.assertNotEqual(ctypes.CField(), ctypes.CField())
        except TypeError:
            self.fail("__eq__(ctypes.CField(), ctypes.CField()) raised TypeError")

    def test___ne__(self):
        try:
            self.assertNotEqual(ctypes.CField(), ctypes.CField())
        except TypeError:
            self.fail("__ne__(ctypes.CField(), ctypes.CField()) raised TypeError")

    def test___lt__(self):
        try:
            self.assertNotEqual(ctypes.CField(),
