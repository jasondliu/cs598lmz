import ctypes
# Test ctypes.CField
__CField__ = ctypes.CField

class __CField(ctypes.CField):
    def __init__(self, type=None, offset=None, **kwds):
        super(__CField, self).__init__(type, **kwds)
        self.offset = offset

class MyStruct(ctypes.Structure):
    _fields_ = [__CField__('n', ctypes.c_int, offset=ctypes.c_int.__basicsize__),
                __CField__('s', ctypes.c_char * 3, offset=ctypes.c_int.__basicsize__*3)]

class Test(BaseTestChecker):
    def test(self):
        # Test ctypes.CField.offset
        self.assertEqual(MyStruct.n.offset, ctypes.c_int.__basicsize__)
        self.assertEqual(MyStruct.s.offset, ctypes.c_int.__basicsize__*3)

        # Test ctypes.CField.from_address(address
