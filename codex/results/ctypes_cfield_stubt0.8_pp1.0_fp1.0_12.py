import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CArrayType = type(ARRAY(c_int, 3))
ctypes.CStringType = type(POINTER(c_char))
ctypes.CUnicodeType = type(POINTER(c_wchar))

class TestArrayStruct(unittest.TestCase):
    def test_array_struct(self):
        # Test that array_struct work on ctypes structure instances.

        a = S()
        b = S()
        a.x = 5
        b.x = 4

        S_array = S * 5
        sa = S_array()
        sa[1] = a
        sa[4] = b
        sa[1] = b # It should be possible to set more than once

        self.assertEqual(sa[1].x, 4)
        self.assertEqual(sa[4].x, 4)

    def test_array_struct_ptr_to_ptr(self):
        # Test that array_struct work on ctypes structure pointers
        S_ptr = POINTER(S)

        a = S()
       
