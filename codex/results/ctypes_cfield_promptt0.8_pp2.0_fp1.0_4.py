import ctypes
# Test ctypes.CField

lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), "testlib_cfield.so"))

class TestCField(unittest.TestCase):
    def test_field(self):
        # Test normal struct field
        class X(ctypes.Structure):
            _fields_ = [
                (  "a", ctypes.c_char),
                (  "b", ctypes.c_int),
                ("cc", ctypes.c_int)]

        self.assertEqual(X._fields_, [("a", ctypes.c_char),
                                      ("b", ctypes.c_int),
                                      ("cc", ctypes.c_int)])

    def test_structure_alignment(self):
        class X(ctypes.Structure):
            _fields_ = [
                (  "a", ctypes.c_char),
                (  "b", ctypes.c_int),
                ("cc", ctypes.c_int)]

        self.assertEqual(X._
