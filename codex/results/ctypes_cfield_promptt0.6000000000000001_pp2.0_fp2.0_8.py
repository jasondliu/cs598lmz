import ctypes
# Test ctypes.CField

class TestCField:
    def test_field_size(self):
        '''Test that the field size is correctly computed'''
        class Test(ctypes.Structure):
            _fields_ = [('x', ctypes.c_byte, 3),
                        ('y', ctypes.c_byte, 5)]
        assert ctypes.sizeof(Test) == 2

    def test_field_offset(self):
        '''Test that the field offset is correctly computed'''
        class Test(ctypes.Structure):
            _fields_ = [('x', ctypes.c_byte, 3),
                        ('y', ctypes.c_byte, 5)]
        assert ctypes.sizeof(Test.x) == 1
        assert ctypes.sizeof(Test.y) == 1
        assert ctypes.addressof(Test.x) == ctypes.addressof(Test)
        assert ctypes.addressof(Test.y) == ctypes.addressof(Test) + 1

    def test_field_bit_access(self):
        '''Test
