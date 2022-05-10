import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    def __init__(self, x):
        self.x = x

def type_test(test_case, x, expected_type):
    test_case.assertEqual(type(x), expected_type)

class CTypesTest(unittest.TestCase):

    def test_c_double(self):
        type_test(self, ctypes.c_double(), type(1.0))
        type_test(self, ctypes.c_double(-1.0), type(-1.0))
        type_test(self, ctypes.c_double(1), type(1.0))
        type_test(self, ctypes.c_double(True), type(1.0))
        type_test(self, ctypes.c_double.from_param(10.0), type(1.0))

    def test_c_float(self):
        type_test(self, ctypes.c_float(), type(1.0))
        type_test(self, ctypes.c_float(-1.0),
