import ctypes
# Test ctypes.CField
# Note: This cannot be run until ctypes has been tested in the test_ctypes suite.
#   ctypes is imported at the top of test_descr.

class Test:
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class Test2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

class Test3(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int),
                ("z", ctypes.c_int)]

class Test4(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("z", ctypes.c_int)]

class CFieldTest(unittest.TestCase):
    def test_type(self):
        self.assertEqual(Test.x.__class__, ctypes.CField)
        self.
