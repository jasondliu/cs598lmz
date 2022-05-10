import ctypes
# Test ctypes.CField.

import unittest

class TestCase(unittest.TestCase):

    def test_basics(self):

        class GT(ctypes.Structure):
            _fields_ = [("name", ctypes.c_char_p)]

        self.assertEqual(GT._fields_[0][1].__name__, "c_char_p")
        self.assertEqual(GT._fields_[0][0], "name")
        self.assertEqual(GT._fields_[0][2], None)

        self.assertRaises(TypeError, ctypes.CField, "name", ctypes.c_int, None)

    def test_var_array(self):

        class GT(ctypes.Structure):
            _fields_ = [("name", ctypes.c_char * 10)]

        self.assertEqual(GT._fields_[0][1].__name__, "c_char_Array_10")
        self.assertEqual(GT._fields_[0][0], "name")
        self.assertEqual(GT
