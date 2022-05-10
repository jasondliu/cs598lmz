import ctypes
# Test ctypes.CField
class TestCField:
    def test_CField(self):
        class Point(ctypes.Structure):
            _fields_ = [("x", ctypes.c_int),
                        ("y", ctypes.c_int)]

        # Test the __get__ method
        p = Point(10, 20)
        assert p.x == 10
        assert p.y == 20

        # Test the __set__ method
        p.x = 30
        p.y = 40
        assert p.x == 30
        assert p.y == 40

        # Test the _CData_output_
        assert repr(p.x) == 'c_int(30)'
        assert repr(p.y) == 'c_int(40)'

        # Test the _CData_retval_
        assert int(p.x) == 30
        assert int(p.y) == 40

        # Test the _CData_input_
        p.x = ctypes.c_int(50)
        p.y = ctypes.c_int(60)
        assert p.x
